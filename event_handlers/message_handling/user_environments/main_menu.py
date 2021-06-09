from bot.dating_bot import DatingBot
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
                                "You are in the main menu.\n"
                                "Available functions:\n"
                                "- Search (Start search your love)\n"
                                "- Chat (Chatting with randoms)\n"
                                "- Settings (Edit your data)\n",
                                keyboard=main_menu_keyboard)

        @self.callback_method(res.emoji.settings)
        def settings(bot, user):
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                f'| Your account |\n\n'
                                f'ID: {user.id}\n'
                                f'{user.account_info()}',
                                keyboard=settings_keyboard,
                                attachments=(user.photo,))

        @self.callback_method(res.emoji.search)
        def searching_friend(bot, user):
            user.env_type = User.Environment.SEARCHING_FRIEND
            bot.vk.send_message(user.id,
                                f"Preparing suggestions for you...")

            user.env_vars.suggestions = bot.get_suggestions_for_user(user)
            user.env_vars.nextSuggestionsIndex = 0

            bot.vk.send_message(user.id,
                                f"Ready! Found {len(user.env_vars.suggestions)} new users for you!",
                                keyboard=searching_friend_keyboard)

            SearchingFriend.show_next_friend(bot, user)

        @self.callback_method(res.emoji.fax)
        def searching_chat(bot, user):
            user.env_type = User.Environment.SEARCHING_CHAT
            bot.vk.send_message(user.id,
                                f"Welcome to chat!\n"
                                f"Here you can find conservations.\n"
                                f"Press {res.emoji.search} to find chat!",
                                keyboard=chat_keyboard)
