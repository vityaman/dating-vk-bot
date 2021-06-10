from bot.bot_environment import BotEnvironment
from bot.bot_user import BotUser
from event_handlers.message_handling.base_objects import MessageHandler, static_singleton


class Admin(BotUser):
    def __init__(self, vk_id: int, environment: BotEnvironment):
        super().__init__(vk_id, environment)


@static_singleton
class AdminMessageHandler(MessageHandler):
    def __init__(self):
        super().__init__()
        self.admin = Admin(-1, BotEnvironment.ADMIN_MAIN_PANEL)

    def handle(self, bot, message):
        self.admin.id = message.peer_id  # id of requesting user
        bundle = dict()  # storage of special data in user message data

        if '@' in message.text:
            message.text = message.text[message.text.index(']') + 1:].strip()

        if message.text != '':
            bundle['text'] = message.text

        # get attachments
        for attachment in message.attachments:
            if attachment['type'] == 'photo':
                if 'photos' not in bundle:
                    bundle['photos'] = []
                bundle['photos'].append(attachment['photo']['sizes'][-1]['url'])

        if self.admin.get_environment() in self.input_environments:
            self.input_environments[self.admin.get_environment()].input(bot, self.admin, bundle)
        elif bundle['text'] in self.callback_environments[self.admin.get_environment()].callback_methods:
            self.callback_environments[self.admin.get_environment()].callback_methods[bundle['text']](bot, self.admin)
        else:
            self.callback_environments[self.admin.get_environment()].callback_methods['Guide'](bot, self.admin)

# TODO: it makes me fear:
# DONT DELETE THIS (Connect environments)
from event_handlers.message_handling.admin_environments import *
