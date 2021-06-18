from collections import deque

from bot.bot_environment import BotEnvironment
from bot.chat_manager import ChatManager
from data.blacklist_manager import BlacklistManager
from utils import MetaSingleton
from data.database import Database
from vk_tools.vkapi_provider import VKAPIProvider
from data.user import User
import datetime


class DatingBot(metaclass=MetaSingleton):
    class Report:
        def __init__(self, sender, criminal, time):
            self.sender = sender
            self.criminal = criminal
            self.time = time

    def __init__(self, vk_group_id, vk_provider: VKAPIProvider):
        self.group_id = vk_group_id

        self.db = Database()
        self.vk = vk_provider
        self.chat_manager = ChatManager()
        self.blacklist = BlacklistManager()

        self.reports: deque[DatingBot.Report] = deque()

        self.users_by_id = dict()
        # Load all users from database
        for user in self.db.all_users():
            self.users_by_id[user.id] = user
        self.newbies_by_id = dict()

    def get_registered_user_by_id_or_none_if_not_found(self, _id):
        # 1) check active users
        user = self.users_by_id.get(_id)
        if user is None:
            # 2) check new users
            user = self.newbies_by_id.get(_id)
            if user is None:
                # 3) check database
                try:
                    user = self.db.get_user_by_id(_id)
                    self.users_by_id[user.id] = user
                except self.db.NoSuchUserException:
                    return None
        return user

    def get_user_by_id_or_create_new(self, _id: int) -> User:
        # TODO: ......... its bad solution
        user = self.get_registered_user_by_id_or_none_if_not_found(_id)
        if user is None:
            # This user is newbie
            user = User(vk_id=_id,
                        environment=BotEnvironment.USER_BEGINNING)
            self.newbies_by_id[_id] = user
        return user

    def is_valid_user(self, user: User) -> bool:
        # TODO: deep review account info
        return True

    def save_user_data(self, user: User):
        if user.id in self.newbies_by_id:
            self.db.insert_user(user)
            self.newbies_by_id.pop(user.id)
            self.users_by_id[user.id] = user
        else:
            self.db.update_user(user)

    def get_suggestions_for_user(self, user: User, count=10) -> list:
        # 1) check people who liked user
        suggestions_from_likes = []
        for user_id in user.fan_ids:
            suggestion = self.get_registered_user_by_id_or_none_if_not_found(user_id)
            if suggestion is not None:
                suggestions_from_likes.append(suggestion)

                count -= 1
                if count <= 0:
                    break

        suggestions_from_likes.sort(key=lambda u: len(u.interests & user.interests), reverse=True)
        if count <= 0:
            return suggestions_from_likes

        # 2) suggest users from all registered users
        suggestions_from_others = []
        for suggestion in self.users_by_id.values():
            if suggestion.id not in user.fan_ids \
                    and suggestion.id not in user.liked_user_ids \
                    and suggestion.id != user.id:
                suggestions_from_others.append(suggestion)

                count -= 1
                if count <= 0:
                    break

        suggestions_from_others.sort(key=lambda u: len(u.interests & user.interests), reverse=True)

        return suggestions_from_likes + suggestions_from_others

    def create_report(self, sender, criminal):
        self.reports.append(DatingBot.Report(sender, criminal,
                                             datetime.datetime.now() + datetime.timedelta(hours=3)))

    def get_report(self):
        return self.reports.popleft()
