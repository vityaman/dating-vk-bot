from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler

from vk_tools.vk_keyboards import *


@UserMessageHandler.callback_environment(BotEnvironment.USER_SEARCHING_FRIEND)
class SearchingFriend(CallbackEnvironment):
    def exit_searching_friend(self, bot: DatingBot, user: User):
        del user.env_vars.nextSuggestionsIndex
        del user.env_vars.suggestions

        user.go_back()
        bot.vk.send_message(user.id,
                            string.searching_friend_exit,
                            keyboard=user.get_keyboard())

    def show_next_friend(self, bot: DatingBot, user: User):
        if user.env_vars.nextSuggestionsIndex < len(user.env_vars.suggestions):
            friend = user.env_vars.suggestions[user.env_vars.nextSuggestionsIndex]
            user.env_vars.nextSuggestionsIndex += 1

            bot.vk.send_message(user.id,
                                f"{string.searching_friend_look_next}\n\n"
                                f"{friend.account_info()}",
                                attachments=(friend.photo,),
                                keyboard=user.get_keyboard())
        else:
            self.exit_searching_friend(bot, user)

    def initialize_methods(self):
        @self.callback_method("Guide")
        def searching_partner_guide(bot: DatingBot, user: User):
            bot.vk.send_message(user.id,
                                string.searching_friend_guide,
                                keyboard=user.get_keyboard())

        @self.callback_method(emoji.like)
        def like_friend(bot: DatingBot, user: User):
            friend = user.env_vars.suggestions[user.env_vars.nextSuggestionsIndex - 1]
            user.liked_user_ids.add(friend.id)

            if friend.id in user.fan_ids:
                # Its match
                bot.vk.send_message(user.id,
                                    f"{string.searching_friend_match_1}\n"
                                    f"vk.com/id{friend.id}\n"
                                    f"{string.searching_friend_match_motivation_1}")
                bot.vk.send_message(friend.id,
                                    f"{string.searching_friend_match_2}\n"
                                    f"{user.account_info()}\n"
                                    f"vk.com/id{user.id}\n"
                                    f"{string.searching_friend_match_motivation_2}",
                                    attachments=(user.photo,))
                friend.fan_ids.discard(user.id)
                user.fan_ids.discard(friend.id)
            else:
                friend.fan_ids.add(user.id)

            self.show_next_friend(bot, user)

        @self.callback_method(emoji.dislike)
        def skip_partner(bot: DatingBot, user: User):
            self.show_next_friend(bot, user)

        @self.callback_method(emoji.report)
        def report_friend(bot: DatingBot, user: User):
            bot.create_report(user, user.env_vars.suggestions[user.env_vars.nextSuggestionsIndex - 1])
            bot.vk.send_message(user.id,
                                string.report_was_sent,
                                keyboard=user.get_keyboard())
            skip_partner(bot, user)

        @self.callback_method(emoji.back)
        def exit_searching_friend(bot, user):
            self.exit_searching_friend(bot, user)
