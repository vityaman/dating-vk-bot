from bot.dating_bot import DatingBot
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
                                "You are in queue...\n"
                                "Please, wait...",
                                keyboard=chat_keyboard)
        else:
            user.env_vars.chat_partner = partner
            partner.env_vars.chat_partner = user

            user.env_type = User.Environment.CHATTING
            bot.vk.send_message(user.id,
                                f"Chat has been found:\n"
                                f"{partner.account_info()}\n\n"
                                f"Talk!\n",
                                keyboard=chat_keyboard,
                                attachments=(partner.photo,))

            partner.env_type = User.Environment.CHATTING
            bot.vk.send_message(partner.id,
                                f"Chat has been found:\n"
                                f"{user.account_info()}\n\n"
                                f"Talk!\n",
                                keyboard=chat_keyboard,
                                attachments=(user.photo,))

    def exit_searching_chat(self, bot, user):
        if user in bot.chat_manager.queue:
            bot.chat_manager.queue.remove(user)
        user.env_type = User.Environment.MAIN_MENU
        bot.vk.send_message(user.id,
                            "OK, goodbye!\n"
                            "See ya later...",
                            keyboard=main_menu_keyboard)

    def initialize_methods(self):
        @self.callback_method("Guide")
        def searching_chat_guide(bot, user):
            bot.vk.send_message(user.id,
                                f"You are in the chat section!\n"
                                f"Available functions:\n"
                                f"- {res.emoji.search} (Search conservation)\n"
                                f"- {res.emoji.report} (Report user)\n"
                                f"- {res.emoji.back} (Back to main menu)\n",
                                keyboard=chat_keyboard)

        @self.callback_method(res.emoji.search)
        def find_chat(bot, user):
            self.find_chat(bot, user)

        @self.callback_method(res.emoji.back)
        def exit_searching_chat(bot, user):
            self.exit_searching_chat(bot, user)


@UserMessageHandler.input_environment(User.Environment.CHATTING)
class Chatting(InputEnvironment):

    def finish_chatting(self, bot, user):
        del user.env_vars.chat_partner
        user.env_type = User.Environment.SEARCHING_CHAT

        bot.vk.send_message(user.id,
                            f"Conversation ended.\n"
                            f"It was nice... {res.emoji.sad}",
                            keyboard=chat_keyboard)

    def close_current_chat(self, bot, user):
        self.finish_chatting(bot, user.env_vars.chat_partner)
        self.finish_chatting(bot, user)

    def input(self, bot, user, bundle):
        if bundle.get('text') == res.emoji.search:
            self.close_current_chat(bot, user)
            SearchingChat.find_chat(bot, user)
        elif bundle.get('text') == res.emoji.report:
            # TODO: report()
            self.close_current_chat(bot, user)
        elif bundle.get('text') == res.emoji.back:
            self.close_current_chat(bot, user)
            SearchingChat.exit_searching_chat(bot, user)
        else:
            bot.vk.send_message(user.env_vars.chat_partner.id,
                                bot.chat_manager.formatted_text(bundle.get('text', '')),
                                attachments=[bot.vk.save_photo_from_url(url) for url in
                                             bundle.get('photos', [])],
                                keyboard=chat_keyboard)
