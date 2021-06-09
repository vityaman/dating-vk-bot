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
                                f"You are in settings menu.\n"
                                f"Available commands:\n"
                                f"- Name (Enter your name) {res.emoji.smile}\n"
                                f"- Age (Enter your age) {res.emoji.glasses}\n"
                                f"- About (Write about you) {res.emoji.talk}\n"
                                f"- Photo (Set avatar photo) {res.emoji.camera}\n"
                                f"- Save (Save changes) {res.emoji.save}",
                                keyboard=settings_keyboard)

        @self.callback_method("Name")
        def settings_name(bot, user):
            user.env_type = User.Environment.SETTINGS_NAME
            bot.vk.send_message(user.id,
                                f"What is your name?",
                                keyboard=input_cancel_keyboard)

        @self.callback_method("Age")
        def settings_age(bot, user):
            user.env_type = User.Environment.SETTINGS_AGE
            bot.vk.send_message(user.id,
                                f"How old are you?\n"
                                f"Just don't cheat, please...",
                                keyboard=input_cancel_keyboard)

        @self.callback_method("About")
        def settings_about(bot, user):
            user.env_type = User.Environment.SETTINGS_ABOUT
            bot.vk.send_message(user.id,
                                "Tell me about yourself!\n"
                                "I'm really interested in it...",
                                keyboard=input_cancel_keyboard)

        @self.callback_method("Interests")
        def settings_interests(bot, user):
            user.env_type = User.Environment.SETTINGS_INTERESTS
            bot.vk.send_message(user.id,
                                "Choice interests tags for your profile\n"
                                "It will improve your suggestions!",
                                keyboard=input_cancel_keyboard)
            bot.vk.send_message(user.id,
                                f"Just type numbers of tags:\n"
                                f"{User.Interest.presentation()}\n\n"
                                f"Sample: 1 4 2 3 6",
                                keyboard=input_cancel_keyboard)

        @self.callback_method("Photo")
        def settings_photo(bot, user):
            user.env_type = User.Environment.SETTINGS_PHOTO
            bot.vk.send_message(user.id,
                                "Everyone want to see you!\n"
                                "I'm sure you're beauty.\n"
                                "Send photo pls!!\n",
                                keyboard=input_cancel_keyboard)

        @self.callback_method("Save")
        def settings_save(bot, user):
            if user.name and user.age and user.about and user.photo and user.interests \
                    and bot.is_valid_user(user):
                bot.save_user_data(user)
                user.env_type = User.Environment.MAIN_MENU
                bot.vk.send_message(user.id, 'Accepted!')
                bot.vk.send_message(user.id,
                                    f'| Your account |\n\n'
                                    f'ID: {user.id}\n'
                                    f'{user.account_info()}',
                                    keyboard=main_menu_keyboard,
                                    attachments=(user.photo,))
            else:
                bot.vk.send_message(user.id,
                                    'You must fill all fields!',
                                    keyboard=settings_keyboard)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_NAME)
class SettingsName(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == "Cancel":
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                f"Return you back.",
                                keyboard=settings_keyboard)
        else:
            # TODO: add more info to bundle as is_text_there
            if 'text' in bundle:
                user.name = bundle['text'].replace('\'', '')
                user.env_type = User.Environment.SETTINGS
                bot.vk.send_message(user.id,
                                    "Nice to meet you!",
                                    keyboard=settings_keyboard)
            else:
                bot.vk.send_message(user.id, "Invalid Input!")


@UserMessageHandler.input_environment(User.Environment.SETTINGS_AGE)
class SettingsAge(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == "Cancel":
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id, "Return you back.",
                                keyboard=settings_keyboard)
        else:
            if 'text' in bundle:
                try:
                    user.age = int(bundle['text'])
                except ValueError as e:
                    bot.vk.send_message(user.id,
                                        "Invalid Input!")
                    return

                if 3 <= user.age <= 100:
                    user.env_type = User.Environment.SETTINGS
                    bot.vk.send_message(user.id,
                                        "Oh, nice! It's time to find love!\n"
                                        "In yours age it's necessary!",
                                        keyboard=settings_keyboard)
                else:
                    bot.vk.send_message(user.id,
                                        "Incorrect age, ц!\n",
                                        keyboard=input_cancel_keyboard)
            else:
                bot.vk.send_message(user.id,
                                    "Invalid Input!")


@UserMessageHandler.input_environment(User.Environment.SETTINGS_ABOUT)
class SettingsAbout(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == "Cancel":
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                "Return you back.",
                                keyboard=settings_keyboard)
        else:
            if 'text' in bundle:
                user.about = bundle['text'].replace('\'', '')
                user.env_type = User.Environment.SETTINGS
                bot.vk.send_message(user.id,
                                    "Ohh, yeah, dude, I knew, that you are cool person!",
                                    keyboard=settings_keyboard)
            else:
                bot.vk.send_message(user.id,
                                    "Invalid Input!")


@UserMessageHandler.input_environment(User.Environment.SETTINGS_INTERESTS)
class SettingsInterests(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == "Cancel":
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                "Return you back.",
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
                                    "Invalid Input!")
                return

            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                "Interests accepted!",
                                keyboard=settings_keyboard)


@UserMessageHandler.input_environment(User.Environment.SETTINGS_PHOTO)
class SettingsPhoto(InputEnvironment):
    def input(self, bot, user, bundle):
        if bundle.get('text') == "Cancel":
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                "Return you back",
                                keyboard=settings_keyboard)
        elif 'photos' in bundle and "userapi.com" in bundle['photos'][0]:
            user.photo = bot.vk.save_photo_from_url(bundle['photos'][0])
            user.env_type = User.Environment.SETTINGS
            bot.vk.send_message(user.id,
                                f"You... so cute... oh, sorry, "
                                f"I have to go... {res.emoji.shyhands}",
                                keyboard=settings_keyboard)
        else:
            bot.vk.send_message(user.id,
                                "What you did? Just send photo po-bratsky.",
                                keyboard=settings_keyboard)
