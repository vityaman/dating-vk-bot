import resources.strings as string
import resources.emojis as emoji

from data.user import User
from event_handlers.message_handling.base_objects import static_singleton, CallbackEnvironment, InputEnvironment
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from vk_tools.vk_keyboards import *


# noinspection PyArgumentList
@UserMessageHandler.callback_environment(User.Environment.SETTINGS)
class Settings(CallbackEnvironment):
    def initialize_methods(self):

        @self.callback_method("Guide")
        def settings_guide(bot, user):
            bot.vk.send_message(user.id,
                                string.settings_guide,
                                keyboard=settings_keyboard)

        @self.callback_method(string.name)
        def settings_name(bot, user):
            user.env_type = User.Environment.SETTINGS_NAME
            bot.vk.send_message(user.id,
                                string.settings_name,
                                keyboard=input_cancel_keyboard)

        @self.callback_method(string.age)
        def settings_age(bot, user):
            user.env_type = User.Environment.SETTINGS_AGE
            bot.vk.send_message(user.id,
                                string.settings_age,
                                keyboard=input_cancel_keyboard)

        @self.callback_method(string.about)
        def settings_about(bot, user):
            user.env_type = User.Environment.SETTINGS_ABOUT
            bot.vk.send_message(user.id,
                                string.about,
                                keyboard=input_cancel_keyboard)

        @self.callback_method(string.interests)
        def settings_interests(bot, user):
            user.env_type = User.Environment.SETTINGS_INTERESTS
            bot.vk.send_message(user.id,
                                f"{string.settings_interests}"
                                f"{User.Interest.presentation()}\n\n"
                                f"Sample: 1 4 2 3 6",
                                keyboard=input_cancel_keyboard)

        @self.callback_method(string.photo)
        def settings_photo(bot, user):
            user.env_type = User.Environment.SETTINGS_PHOTO
            bot.vk.send_message(user.id,
                                string.settings_photo,
                                keyboard=input_cancel_keyboard)

        @self.callback_method(string.save)
        def settings_save(bot, user):
            if user.name and user.age and user.about and user.photo and user.interests \
                    and bot.is_valid_user(user):
                bot.save_user_data(user)
                user.env_type = User.Environment.MAIN_MENU
                bot.vk.send_message(user.id, string.accepted)
                bot.vk.send_message(user.id,
                                    f'{string.form_heading}'
                                    f'ID: {user.id}\n'
                                    f'{user.account_info()}',
                                    keyboard=main_menu_keyboard,
                                    attachments=(user.photo,))
            else:
                bot.vk.send_message(user.id,
                                    string.settings_fill_all,
                                    keyboard=settings_keyboard)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_NAME)
class SettingsName(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == string.cancel:
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=settings_keyboard)
        else:
            # TODO: add more info to bundle as is_text_there
            if 'text' in bundle:
                user.name = bundle['text'].replace('\'', '')
                user.env_type = User.Environment.SETTINGS
                bot.vk.send_message(user.id,
                                    string.settings_ok_name,
                                    keyboard=settings_keyboard)
            else:
                bot.vk.send_message(user.id, string.settings_invalid_input)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_AGE)
class SettingsAge(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == string.cancel:
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id, string.settings_return,
                                keyboard=settings_keyboard)
        else:
            if 'text' in bundle:
                try:
                    user.age = int(bundle['text'])
                except ValueError as e:
                    bot.vk.send_message(user.id,
                                        string.settings_invalid_input)
                    return

                if 3 <= user.age <= 100:
                    user.env_type = User.Environment.SETTINGS
                    bot.vk.send_message(user.id,
                                        string.settings_ok_age,
                                        keyboard=settings_keyboard)
                else:
                    bot.vk.send_message(user.id,
                                        string.settings_invalid_input,
                                        keyboard=input_cancel_keyboard)
            else:
                bot.vk.send_message(user.id,
                                    string.settings_invalid_input)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_ABOUT)
class SettingsAbout(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == string.cancel:
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=settings_keyboard)
        else:
            if 'text' in bundle:
                user.about = bundle['text'].replace('\'', '')
                user.env_type = User.Environment.SETTINGS
                bot.vk.send_message(user.id,
                                    string.settings_ok_about,
                                    keyboard=settings_keyboard)
            else:
                bot.vk.send_message(user.id,
                                    string.settings_invalid_input)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_INTERESTS)
class SettingsInterests(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == string.cancel:
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=settings_keyboard)
        else:
            try:
                text = bundle.get('text').strip()
                user.interests = set()
                for interest in map(int, text.split()):
                    if User.Interest.contains(interest):
                        user.interests.add(interest)
            # TODO: bad exception handling
            except Exception as e:
                bot.vk.send_message(user.id,
                                    string.settings_invalid_input)
                return

            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                string.settings_ok_interests,
                                keyboard=settings_keyboard)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_PHOTO)
class SettingsPhoto(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == string.cancel:
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                string.settings_return,
                                keyboard=settings_keyboard)
        elif 'photos' in bundle and "userapi.com" in bundle['photos'][0]:
            user.photo = bot.vk.save_photo_from_url(bundle['photos'][0])
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                string.settings_ok_photo,
                                keyboard=settings_keyboard)
        else:
            bot.vk.send_message(user.id,
                                "What you did? Just send photo po-bratsky.",
                                keyboard=settings_keyboard)
