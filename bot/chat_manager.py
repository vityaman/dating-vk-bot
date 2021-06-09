from collections import deque
from data.user import User


class ChatManager:
    def __init__(self):
        self.queue = deque()

    def get_chat_partner(self, user) -> User:
        if user not in self.queue:
            if len(self.queue) > 0:
                return self.queue.pop()
            else:
                self.queue.append(user)
        return None

    def formatted_text(self, text: str):
        return text  # TODO: text formatting