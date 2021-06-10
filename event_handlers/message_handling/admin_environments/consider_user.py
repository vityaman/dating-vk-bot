from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from event_handlers.message_handling.admin_message_handler import Admin, AdminMessageHandler
from event_handlers.message_handling.base_objects import CallbackEnvironment
import resources.emojis as emoji


@AdminMessageHandler.callback_environment(BotEnvironment.ADMIN_CONSIDER_USER)
class ConsiderUser(CallbackEnvironment):
    def show_user(self, bot: DatingBot, admin: Admin):
        bot.vk.send_message(admin.id,
                            f"| User |\n\n"
                            f"ID: {admin.env_vars.user.id}\n\n"
                            f"{admin.env_vars.user.account_info()}",
                            keyboard=admin.get_keyboard(),
                            attachments=(admin.env_vars.user.photo, ))

    def initialize_methods(self):
        @self.callback_method("Guide")
        def consider_report_guide(bot: DatingBot, admin: Admin):
            bot.vk.send_message(admin.id,
                                f"You are considering user.\n"
                                f"Available functions:\n"
                                f"{emoji.back} Back",
                                keyboard=admin.get_keyboard())

        @self.callback_method(emoji.back)
        def back(bot: DatingBot, admin: Admin):
            del admin.env_vars.user
            admin.go_back()
            bot.vk.send_message(admin.id,
                                "Return you back",
                                keyboard=admin.get_keyboard())
