from enum import Enum
from vk_tools.vk_keyboards import *

class BotEnvironment(Enum):

    USER_BEGINNING = (0, begin_keyboard)
    USER_SETTINGS = (1, settings_keyboard)
    USER_SETTINGS_NAME = (2, input_cancel_keyboard)
    USER_SETTINGS_AGE = (3, input_cancel_keyboard)
    USER_SETTINGS_ABOUT = (4, input_cancel_keyboard)
    USER_SETTINGS_INTERESTS = (5, input_cancel_keyboard)
    USER_SETTINGS_PHOTO = (6, input_cancel_keyboard)
    USER_MAIN_MENU = (7, main_menu_keyboard)
    USER_SEARCHING_FRIEND = (8, searching_friend_keyboard)
    USER_SEARCHING_CHAT = (9, chat_keyboard)
    USER_CHATTING = (10, chat_keyboard)

    ADMIN_MAIN_PANEL = (1000_0, admin_panel_keyboard)
    ADMIN_CONSIDER_REPORTS = (1000_1, consider_report_keyboard)
    ADMIN_CONSIDER_USER = (1000_2, consider_user_keyboard)
