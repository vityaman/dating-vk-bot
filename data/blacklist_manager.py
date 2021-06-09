import os

from utils import MetaSingleton


class BlacklistManager(metaclass=MetaSingleton):
    BLACKLIST_FILE_NAME = os.path.join(os.path.dirname(__file__), "blacklist.txt")

    def __init__(self):
        self.blocked_user_ids = set()
        with open(self.BLACKLIST_FILE_NAME, 'r') as file:
            for line in file.readlines():
                _id = line.strip()
                if _id != '':
                    self.blocked_user_ids.add(int(_id))

    def extend_and_update_list(self, user_ids):
        with open(self.BLACKLIST_FILE_NAME, 'a') as file:
            for _id in user_ids:
                if _id not in self.blocked_user_ids:
                    self.blocked_user_ids.add(_id)
                    file.write(str(_id) + "\n")

    def discard_and_update_list(self, user_ids):
        for _id in user_ids:
            self.blocked_user_ids.discard(_id)
        self.update_whole_list()

    def update_whole_list(self):
        with open(self.BLACKLIST_FILE_NAME, 'w') as file:
            for _id in self.blocked_user_ids:
                file.write(str(_id) + "\n")
