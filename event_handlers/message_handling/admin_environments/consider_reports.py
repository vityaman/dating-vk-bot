from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from event_handlers.message_handling.admin_environments.consider_user import ConsiderUser
from event_handlers.message_handling.admin_message_handler import AdminMessageHandler, Admin
from event_handlers.message_handling.base_objects import CallbackEnvironment
import resources.emojis as emoji


@AdminMessageHandler.callback_environment(BotEnvironment.ADMIN_CONSIDER_REPORTS)
class ConsiderReports(CallbackEnvironment):
    def next_report(self, bot, admin):
        report = bot.get_report()
        bot.vk.send_message(admin.id,
                            f"| Report {report.time.strftime('%m/%d %H:%M')} |\n"
                            f"From [id{report.sender.id}|{report.sender.name}]\n"
                            f"To [id{report.criminal.id}|{report.criminal.name}]!",
                            keyboard=admin.get_keyboard(),
                            attachments=(report.sender.photo, report.criminal.photo))
        admin.env_vars.report = report

    def initialize_methods(self):
        @self.callback_method("Guide")
        def consider_report_guide(bot: DatingBot, admin):
            bot.vk.send_message(admin.id,
                                f"You are considering report.\n"
                                f"Available functions:\n"
                                f"{emoji.stats} Next\n"
                                f"{emoji.police} Check Sender\n"
                                f"{emoji.notify} Check Criminal\n"
                                f"{emoji.back} Back",
                                keyboard=admin.get_keyboard())

        @self.callback_method(emoji.police)
        def get_next_report(bot: DatingBot, admin: Admin):
            self.next_report(bot, admin)

        @self.callback_method(emoji.back)
        def back(bot: DatingBot, admin: Admin):
            del admin.env_vars.report
            admin.go_back()
            bot.vk.send_message(admin.id,
                                "Back to AdminPanel",
                                keyboard=admin.get_keyboard())

        @self.callback_method('Sender')
        def consider_sender(bot: DatingBot, admin: Admin):
            admin.env_vars.user = admin.env_vars.report.sender
            admin.go_to(BotEnvironment.ADMIN_CONSIDER_USER)
            bot.vk.send_message(admin.id,
                                f"Let's consider https://vk.com/id{admin.env_vars.user.id}:")
            ConsiderUser.show_user(bot, admin)

        @self.callback_method('Criminal')
        def consider_criminal(bot: DatingBot, admin: Admin):
            admin.env_vars.user = admin.env_vars.report.criminal
            admin.go_to(BotEnvironment.ADMIN_CONSIDER_USER)
            bot.vk.send_message(admin.id,
                                f"Let's consider https://vk.com/id{admin.env_vars.user.id}:")
            ConsiderUser.show_user(bot, admin)
