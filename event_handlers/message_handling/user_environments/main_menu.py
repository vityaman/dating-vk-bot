import resources.strings as string
import resources.emojis as emoji
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from event_handlers.message_handling.user_environments.searching_friend import SearchingFriend
from vk_tools.vk_keyboards import *


# noinspection PyArgumentList
@UserMessageHandler.callback_environment(User.Environment.MAIN_MENU)
class MainMenu(CallbackEnvironment):
    def initialize_methods(self):
        @self.callback_method("Guide")
        def main_menu_guide(bot, user):
            bot.vk.send_message(user.id,
                                string.main_menu_guide,
                                keyboard=main_menu_keyboard)

        @self.callback_method(emoji.settings)
        def settings(bot, user):
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                f'{string.form_heading}'
                                f'ID: {user.id}\n'
                                f'{user.account_info()}',
                                keyboard=settings_keyboard,
                                attachments=(user.photo,))

        @self.callback_method(emoji.search)
        def searching_friend(bot, user):
            user.env_type = User.Environment.SEARCHING_FRIEND
            bot.vk.send_message(user.id,
                                string.main_menu_preparing_suggestions)

            user.env_vars.suggestions = bot.get_suggestions_for_user(user)
            user.env_vars.nextSuggestionsIndex = 0

            bot.vk.send_message(user.id,
                                f"{string.main_menu_found} {len(user.env_vars.suggestions)}!",
                                keyboard=searching_friend_keyboard)

            SearchingFriend.show_next_friend(bot, user)

        @self.callback_method(emoji.fax)
        def searching_chat(bot, user):
            user.env_type = User.Environment.SEARCHING_CHAT
            bot.vk.send_message(user.id,
                                string.main_menu_welcome_chat,
                                keyboard=chat_keyboard)
