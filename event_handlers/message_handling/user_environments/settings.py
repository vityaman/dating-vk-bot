from bot.dating_bot import DatingBot
from bot.bot_environment import BotEnvironment
from data.user import User
from event_handlers.message_handling.base_objects import CallbackEnvironment, InputEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from vk_tools.vk_keyboards import *


@UserMessageHandler.callback_environment(BotEnvironment.USER_SETTINGS)
class Settings(CallbackEnvironment):
    def initialize_methods(self):

        @self.callback_method("Guide")
        def settings_guide(bot: DatingBot, user: User):
            bot.vk.send_message(user.id,
                                string.settings_guide,
                                keyboard=user.get_keyboard())

        @self.callback_method(string.name)
        def settings_name(bot: DatingBot, user: User):
            user.go_to(BotEnvironment.USER_SETTINGS_NAME)
            bot.vk.send_message(user.id,
                                string.settings_name,
                                keyboard=user.get_keyboard())

        @self.callback_method(string.age)
        def settings_age(bot: DatingBot, user: User):
            user.go_to(BotEnvironment.USER_SETTINGS_AGE)
            bot.vk.send_message(user.id,
                                string.settings_age,
                                keyboard=user.get_keyboard())

        @self.callback_method(string.about)
        def settings_about(bot: DatingBot, user: User):
            user.go_to(BotEnvironment.USER_SETTINGS_ABOUT)
            bot.vk.send_message(user.id,
                                string.settings_about,
                                keyboard=user.get_keyboard())

        @self.callback_method(string.interests)
        def settings_interests(bot: DatingBot, user: User):
            user.go_to(BotEnvironment.USER_SETTINGS_INTERESTS)
            bot.vk.send_message(user.id,
                                f"{string.settings_interests}\n\n"
                                f"{User.Interest.presentation()}\n\n"
                                f"Sample: a b c e",
                                keyboard=user.get_keyboard())

        @self.callback_method(string.photo)
        def settings_photo(bot: DatingBot, user: User):
            user.go_to(BotEnvironment.USER_SETTINGS_PHOTO)
            bot.vk.send_message(user.id,
                                string.settings_photo,
                                keyboard=user.get_keyboard())

        @self.callback_method(string.save)
        def settings_save(bot: DatingBot, user: User):
            if user.name and user.age \
                    and user.about and user.photo \
                    and user.interests and bot.is_valid_user(user):
                bot.save_user_data(user)

                user.go_back()
                if user.get_keyboard() == BotEnvironment.USER_BEGINNING:
                    user.go_back()
                    user.go_to(BotEnvironment.USER_MAIN_MENU)

                bot.vk.send_message(user.id, string.accepted)
                bot.vk.send_message(user.id,
                                    f'{string.form_heading}'
                                    f'ID: {user.id}\n'
                                    f'{user.account_info()}',
                                    keyboard=user.get_keyboard(),
                                    attachments=(user.photo,))
            else:
                bot.vk.send_message(user.id,
                                    string.settings_fill_all,
                                    keyboard=user.get_keyboard())


@UserMessageHandler.input_environment(BotEnvironment.USER_SETTINGS_NAME)
class SettingsName(InputEnvironment):
    def input(self, bot: DatingBot, user: User, bundle):
        if bundle.get('text') == string.cancel:
            user.go_back()
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=user.get_keyboard())
        else:
            # TODO: add more info to bundle as is_text_there
            if 'text' in bundle:
                user.name = bundle['text'].replace('\'', '')
                user.go_back()
                bot.vk.send_message(user.id,
                                    string.settings_ok_name,
                                    keyboard=user.get_keyboard())
            else:
                bot.vk.send_message(user.id, string.settings_invalid_input)


@UserMessageHandler.input_environment(BotEnvironment.USER_SETTINGS_AGE)
class SettingsAge(InputEnvironment):
    def input(self, bot: DatingBot, user: User, bundle):
        if bundle.get('text') == string.cancel:
            user.go_back()
            bot.vk.send_message(user.id, string.settings_return,
                                keyboard=user.get_keyboard())
        else:
            if 'text' in bundle:
                try:
                    user.age = int(bundle['text'])
                except ValueError as e:
                    bot.vk.send_message(user.id,
                                        string.settings_invalid_input,
                                        keyboard=user.get_keyboard())
                    return

                if 3 <= user.age <= 50:
                    user.go_back()
                    bot.vk.send_message(user.id,
                                        string.settings_ok_age,
                                        keyboard=user.get_keyboard())
                else:
                    bot.vk.send_message(user.id,
                                        string.settings_invalid_input,
                                        keyboard=user.get_keyboard())
            else:
                bot.vk.send_message(user.id,
                                    string.settings_invalid_input,
                                    keyboard=user.get_keyboard())


@UserMessageHandler.input_environment(BotEnvironment.USER_SETTINGS_ABOUT)
class SettingsAbout(InputEnvironment):
    def input(self, bot: DatingBot, user: User, bundle):
        if bundle.get('text') == string.cancel:
            user.go_back()
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=user.get_keyboard())
        else:
            if 'text' in bundle:
                user.about = bundle['text'].replace('\'', '')
                user.go_back()
                bot.vk.send_message(user.id,
                                    string.settings_ok_about,
                                    keyboard=user.get_keyboard())
            else:
                bot.vk.send_message(user.id,
                                    string.settings_invalid_input)


@UserMessageHandler.input_environment(BotEnvironment.USER_SETTINGS_INTERESTS)
class SettingsInterests(InputEnvironment):
    def input(self, bot: DatingBot, user: User, bundle):
        if bundle.get('text') == string.cancel:
            user.go_back()
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=user.get_keyboard())
        else:
            try:
                text = bundle.get('text').strip()
                user.interests = set()
                for interest in text.split():
                    if User.Interest.contains(interest):
                        user.interests.add(interest)
            # TODO: bad exception handling
            except Exception as e:
                bot.vk.send_message(user.id,
                                    string.settings_invalid_input)
                return

            user.go_back()
            bot.vk.send_message(user.id,
                                string.settings_ok_interests,
                                keyboard=user.get_keyboard())


@UserMessageHandler.input_environment(BotEnvironment.USER_SETTINGS_PHOTO)
class SettingsPhoto(InputEnvironment):
    def input(self, bot: DatingBot, user: User, bundle):
        if bundle.get('text') == string.cancel:
            user.go_back()
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=user.get_keyboard())
        elif 'photos' in bundle and "userapi.com" in bundle['photos'][0]:
            user.photo = bot.vk.save_photo_from_url(bundle['photos'][0])
            user.go_back()
            bot.vk.send_message(user.id,
                                string.settings_ok_photo,
                                keyboard=user.get_keyboard())
        else:
            bot.vk.send_message(user.id,
                                "What you did? Just send photo po-bratsky.",
                                keyboard=user.get_keyboard())
