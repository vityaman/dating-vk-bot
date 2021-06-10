from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment, InputEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from vk_tools.vk_keyboards import *


@UserMessageHandler.callback_environment(BotEnvironment.USER_SEARCHING_CHAT)
class SearchingChat(CallbackEnvironment):
    def find_chat(self, bot: DatingBot, user: User):
        partner = bot.chat_manager.get_chat_partner(user)

        if partner is None:
            bot.vk.send_message(user.id,
                                string.chat_queue,
                                keyboard=user.get_keyboard())
        else:
            user.env_vars.chat_partner = partner
            partner.env_vars.chat_partner = user

            user.go_to(BotEnvironment.USER_CHATTING)
            bot.vk.send_message(user.id,
                                f"{string.chat_found}"
                                f"{partner.account_info()}\n\n"
                                f"{string.chat_talk}",
                                keyboard=user.get_keyboard(),
                                attachments=(partner.photo,))

            partner.go_to(BotEnvironment.USER_CHATTING)
            bot.vk.send_message(partner.id,
                                f"{string.chat_found}"
                                f"{user.account_info()}\n\n"
                                f"{string.chat_talk}",
                                keyboard=partner.get_keyboard(),
                                attachments=(user.photo,))

    def exit_searching_chat(self, bot: DatingBot, user: User):
        if user in bot.chat_manager.queue:
            bot.chat_manager.queue.remove(user)
        user.go_back()
        bot.vk.send_message(user.id,
                            string.chat_exit,
                            keyboard=user.get_keyboard())

    def initialize_methods(self):
        @self.callback_method("Guide")
        def searching_chat_guide(bot: DatingBot, user: User):
            bot.vk.send_message(user.id,
                                string.chat_guide,
                                keyboard=user.get_keyboard())

        @self.callback_method(emoji.search)
        def find_chat(bot: DatingBot, user: User):
            self.find_chat(bot, user)

        @self.callback_method(emoji.back)
        def exit_searching_chat(bot: DatingBot, user: User):
            self.exit_searching_chat(bot, user)


@UserMessageHandler.input_environment(BotEnvironment.USER_CHATTING)
class Chatting(InputEnvironment):
    def finish_chatting(self, bot: DatingBot, user: User):
        del user.env_vars.chat_partner
        user.go_back()

        bot.vk.send_message(user.id,
                            string.chatting_exit,
                            keyboard=user.get_keyboard())

    def close_current_chat(self, bot: DatingBot, user: User):
        self.finish_chatting(bot, user.env_vars.chat_partner)
        self.finish_chatting(bot, user)

    def input(self, bot, user, bundle):
        if bundle.get('text') == emoji.search:
            self.close_current_chat(bot, user)
            SearchingChat.find_chat(bot, user)
        elif bundle.get('text') == emoji.report:
            bot.create_report(user, user.env_vars.chat_partner)
            self.close_current_chat(bot, user)
        elif bundle.get('text') == emoji.back:
            self.close_current_chat(bot, user)
            SearchingChat.exit_searching_chat(bot, user)
        else:
            bot.vk.send_message(user.env_vars.chat_partner.id,
                                bot.chat_manager.formatted_text(bundle.get('text', 'No text')),
                                attachments=[bot.vk.save_photo_from_url(url) for url in
                                             bundle.get('photos', [])],
                                keyboard=user.get_keyboard())
