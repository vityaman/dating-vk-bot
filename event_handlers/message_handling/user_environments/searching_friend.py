import resources.strings as string
import resources.emojis as emoji

from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment, static_singleton
from event_handlers.message_handling.user_message_handler import UserMessageHandler

from vk_tools.vk_keyboards import *


@UserMessageHandler.callback_environment(User.Environment.SEARCHING_FRIEND)
class SearchingFriend(CallbackEnvironment):
    def exit_searching_friend(self, bot, user):
        del user.env_vars.nextSuggestionsIndex
        del user.env_vars.suggestions
        user.env_type = User.Environment.MAIN_MENU
        bot.vk.send_message(user.id, string.searching_friend_exit,
                            keyboard=main_menu_keyboard)

    def show_next_friend(self, bot, user):
        if user.env_vars.nextSuggestionsIndex < len(user.env_vars.suggestions):
            friend: User = user.env_vars.suggestions[user.env_vars.nextSuggestionsIndex]
            user.env_vars.nextSuggestionsIndex += 1

            bot.vk.send_message(user.id, f"{string.searching_friend_look_next}"
                                         f"{friend.account_info()}",
                                attachments=(friend.photo,),
                                keyboard=searching_friend_keyboard)
        else:
            self.exit_searching_friend(bot, user)

    def initialize_methods(self):
        @self.callback_method("Guide")
        def searching_partner_guide(bot, user):
            bot.vk.send_message(user.id,
                                string.searching_friend_guide,
                                keyboard=searching_friend_keyboard)

        @self.callback_method(emoji.like)
        def like_friend(bot, user):
            friend: User = user.env_vars.suggestions[user.env_vars.nextSuggestionsIndex - 1]
            user.liked_user_ids.add(friend.id)

            if friend.id in user.fan_ids:
                # Its match
                bot.vk.send_message(user.id,
                                    f"{string.searching_friend_match_1}"
                                    f"vk.com/id{friend.id}\n"
                                    f"{string.searching_friend_match_motivation_1}")
                bot.vk.send_message(friend.id,
                                    f"{string.searching_friend_match_2}"
                                    f"{user.account_info()}\n"
                                    f"VK:\n"
                                    f"vk.com/id{user.id}\n"
                                    f"{string.searching_friend_match_motivation_2}",
                                    attachments=(user.photo,))
                friend.fan_ids.discard(user.id)
                user.fan_ids.discard(friend.id)
            else:
                friend.fan_ids.add(user.id)

            self.show_next_friend(bot, user)

        @self.callback_method(emoji.dislike)
        def skip_partner(bot, user):
            self.show_next_friend(bot, user)

        @self.callback_method(emoji.report)
        def report_friend(bot, user):
            # TODO: report
            bot.vk.send_message(user.id,
                                string.report_was_sent,
                                keyboard=searching_friend_keyboard)
            skip_partner(bot, user)

        @self.callback_method(emoji.back)
        def exit_searching_friend(bot, user):
            self.exit_searching_friend(bot, user)
