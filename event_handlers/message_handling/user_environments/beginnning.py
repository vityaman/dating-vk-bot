from bot.dating_bot import DatingBot
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler

from vk_tools.vk_keyboards import *


# noinspection PyArgumentList
@UserMessageHandler.callback_environment(User.Environment.BEGINNING)
class Beginning(CallbackEnvironment):
    def initialize_methods(self):
        @self.callback_method("Begin")
        def begin(bot: DatingBot, user: User):
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id, f"Welcome!\n"
                                         f"We'll register you first.\n"
                                         f"Here are the settings. Fill the from:",
                                keyboard=settings_keyboard)

        @self.callback_method("Guide")
        def begin_guide(bot: DatingBot, user: User):
            bot.vk.send_message(user.id, f"Oh, hello, honey!\n"
                                         f"Are you for the first time here?\n"
                                         f"Press \"Begin\" to continue :)",
                                keyboard=begin_keyboard)
