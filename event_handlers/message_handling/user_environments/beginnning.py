import resources.strings as string
import resources.emojis as emoji

from bot.dating_bot import DatingBot
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler

from vk_tools.vk_keyboards import *


# noinspection PyArgumentList
@UserMessageHandler.callback_environment(User.Environment.BEGINNING)
class Beginning(CallbackEnvironment):
    def initialize_methods(self):
        @self.callback_method(string.begin)
        def begin(bot: DatingBot, user: User):
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id, string.begin_hello,
                                keyboard=settings_keyboard)

        @self.callback_method("Guide")
        def begin_guide(bot: DatingBot, user: User):
            bot.vk.send_message(user.id, string.begin_guide,
                                keyboard=begin_keyboard)
