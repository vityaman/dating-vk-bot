from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from event_handlers.message_handling.admin_environments.consider_reports import ConsiderReports
from event_handlers.message_handling.admin_message_handler import AdminMessageHandler, Admin
from event_handlers.message_handling.base_objects import CallbackEnvironment
import resources.emojis as emoji


@AdminMessageHandler.callback_environment(BotEnvironment.ADMIN_MAIN_PANEL)
class MainPanel(CallbackEnvironment):
    def initialize_methods(self):
        @self.callback_method("Guide")
        def admin_panel_guide(bot: DatingBot, admin: Admin):
            bot.vk.send_message(admin.id,
                                f"You are in the admin panel.\n"
                                f"Available functions:\n"
                                f"{emoji.stats} Stats\n"
                                f"{emoji.police} Check reports\n"
                                f"{emoji.notify} Notify people\n"
                                f"{emoji.settings} Settings (Not ready)",
                                keyboard=admin.get_keyboard())

        @self.callback_method(emoji.stats)
        def stats(bot: DatingBot, admin: Admin):
            registered_users = bot.users_by_id.values()
            newbies = bot.newbies_by_id.values()

            bot.vk.send_message(admin.id,
                                f"| Bot statistics |\n"
                                f"Users: {len(registered_users)}/{len(newbies)}\n",
                                keyboard=admin.get_keyboard())

            str_users_list = f'Registered:\n'
            for user in registered_users:
                str_users_list += f'{user.name}\n'
            bot.vk.send_message(admin.id,
                                str_users_list,
                                keyboard=admin.get_keyboard())

            str_users_list = f'Newbies:\n'
            for user in newbies:
                str_users_list += f'{user.name}\n'
            bot.vk.send_message(admin.id,
                                str_users_list,
                                keyboard=admin.get_keyboard())

        @self.callback_method(emoji.police)
        def check_reports(bot: DatingBot, admin: Admin):
            bot.vk.send_message(admin.id,
                                f"Found {len(bot.reports)} reports!")
            if len(bot.reports) > 0:
                admin.go_to(BotEnvironment.ADMIN_CONSIDER_REPORTS)
                ConsiderReports.next_report(bot, admin)
