import resources.emojis as emoji
import resources.strings as string

from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment, InputEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from vk_tools.vk_keyboards import *


@UserMessageHandler.callback_environment(User.Environment.SEARCHING_CHAT)
class SearchingChat(CallbackEnvironment):
    def find_chat(self, bot, user):
        partner: User = bot.chat_manager.get_chat_partner(user)

        if partner is None:
            bot.vk.send_message(user.id,
                                string.chat_queue,
                                keyboard=chat_keyboard)
        else:
            user.env_vars.chat_partner = partner
            partner.env_vars.chat_partner = user

            user.env_type = User.Environment.CHATTING
            bot.vk.send_message(user.id,
                                f"{string.chat_found}"
                                f"{partner.account_info()}\n\n"
                                f"{string.chat_talk}",
                                keyboard=chat_keyboard,
                                attachments=(partner.photo,))

            partner.env_type = User.Environment.CHATTING
            bot.vk.send_message(partner.id,
                                f"{string.chat_found}"
                                f"{user.account_info()}\n\n"
                                f"{string.chat_talk}",
                                keyboard=chat_keyboard,
                                attachments=(user.photo,))

    def exit_searching_chat(self, bot, user):
        if user in bot.chat_manager.queue:
            bot.chat_manager.queue.remove(user)
        user.env_type = User.Environment.MAIN_MENU
        bot.vk.send_message(user.id,
                            string.chat_exit,
                            keyboard=main_menu_keyboard)

    def initialize_methods(self):
        @self.callback_method("Guide")
        def searching_chat_guide(bot, user):
            bot.vk.send_message(user.id,
                                string.chat_guide,
                                keyboard=chat_keyboard)

        @self.callback_method(emoji.search)
        def find_chat(bot, user):
            self.find_chat(bot, user)

        @self.callback_method(emoji.back)
        def exit_searching_chat(bot, user):
            self.exit_searching_chat(bot, user)


@UserMessageHandler.input_environment(User.Environment.CHATTING)
class Chatting(InputEnvironment):

    def finish_chatting(self, bot, user):
        del user.env_vars.chat_partner
        user.env_type = User.Environment.SEARCHING_CHAT

        bot.vk.send_message(user.id,
                            string.chatting_exit,
                            keyboard=chat_keyboard)

    def close_current_chat(self, bot, user):
        self.finish_chatting(bot, user.env_vars.chat_partner)
        self.finish_chatting(bot, user)

    def input(self, bot, user, bundle):
        if bundle.get('text') == emoji.search:
            self.close_current_chat(bot, user)
            SearchingChat.find_chat(bot, user)
        elif bundle.get('text') == emoji.report:
            # TODO: report()
            self.close_current_chat(bot, user)
        elif bundle.get('text') == emoji.back:
            self.close_current_chat(bot, user)
            SearchingChat.exit_searching_chat(bot, user)
        else:
            bot.vk.send_message(user.env_vars.chat_partner.id,
                                bot.chat_manager.formatted_text(bundle.get('text', '')),
                                attachments=[bot.vk.save_photo_from_url(url) for url in
                                             bundle.get('photos', [])],
                                keyboard=chat_keyboard)
