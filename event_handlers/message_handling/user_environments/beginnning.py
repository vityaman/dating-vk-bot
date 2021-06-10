from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from vk_tools.vk_keyboards import *


@UserMessageHandler.callback_environment(BotEnvironment.USER_BEGINNING)
class Beginning(CallbackEnvironment):
    def initialize_methods(self):
        @self.callback_method(string.begin)
        def begin(bot: DatingBot, user: User):
            user.go_to(BotEnvironment.SETTINGS)
            bot.vk.send_message(user.id,
                                string.begin_hello,
                                keyboard=user.get_keyboard())

        @self.callback_method("Guide")
        def begin_guide(bot: DatingBot, user: User):
            bot.vk.send_message(user.id,
                                string.begin_guide,
                                keyboard=user.get_keyboard())
