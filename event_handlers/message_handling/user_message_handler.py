from event_handlers.message_handling.base_objects import MessageHandler, static_singleton


@static_singleton
class UserMessageHandler(MessageHandler):
    def handle(self, bot, message):
        user_id: int = message.peer_id  # id of requesting user
        bundle = dict()  # storage of special data in user message data

        if message.text != '':
            bundle['text'] = message.text

        # get attachments
        for attachment in message.attachments:
            if attachment['type'] == 'photo':
                if 'photos' not in bundle:
                    bundle['photos'] = []
                bundle['photos'].append(attachment['photo']['sizes'][-1]['url'])

        # get user from amin system
        user = bot.get_user_by_id_or_create_new(user_id)
        if user.get_environment() in self.input_environments:
            self.input_environments[user.get_environment()].input(bot, user, bundle)
        elif bundle['text'] in self.callback_environments[user.get_environment()].callback_methods:
            self.callback_environments[user.get_environment()].callback_methods[bundle['text']](bot, user)
        else:
            self.callback_environments[user.get_environment()].callback_methods['Guide'](bot, user)

# TODO: it makes me fear:
# DONT DELETE THIS
from event_handlers.message_handling.user_environments import *
