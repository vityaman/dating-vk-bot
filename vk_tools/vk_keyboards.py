from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import resources.emojis as emoji
import resources.strings as string

begin_keyboard = VkKeyboard(one_time=False)
begin_keyboard.add_button(string.begin, VkKeyboardColor.PRIMARY)
begin_keyboard = begin_keyboard.get_keyboard()

settings_keyboard = VkKeyboard(one_time=False)
settings_keyboard.add_button(string.name, VkKeyboardColor.SECONDARY)
settings_keyboard.add_button(string.age, VkKeyboardColor.SECONDARY)
settings_keyboard.add_line()
settings_keyboard.add_button(string.about, VkKeyboardColor.SECONDARY)
settings_keyboard.add_button(string.interests, VkKeyboardColor.SECONDARY)
settings_keyboard.add_line()
settings_keyboard.add_button(string.photo, VkKeyboardColor.SECONDARY)
settings_keyboard.add_line()
settings_keyboard.add_button(string.save, VkKeyboardColor.NEGATIVE)
settings_keyboard = settings_keyboard.get_keyboard()

input_cancel_keyboard = VkKeyboard(one_time=False)
input_cancel_keyboard.add_button(string.cancel, VkKeyboardColor.NEGATIVE)
input_cancel_keyboard = input_cancel_keyboard.get_keyboard()

main_menu_keyboard = VkKeyboard(one_time=False)
main_menu_keyboard.add_button(emoji.search, VkKeyboardColor.PRIMARY)
main_menu_keyboard.add_button(emoji.fax, VkKeyboardColor.PRIMARY)
main_menu_keyboard.add_button(emoji.settings, VkKeyboardColor.SECONDARY)
main_menu_keyboard = main_menu_keyboard.get_keyboard()

searching_friend_keyboard = VkKeyboard(one_time=False)
searching_friend_keyboard.add_button(emoji.like, VkKeyboardColor.POSITIVE)
searching_friend_keyboard.add_button(emoji.dislike, VkKeyboardColor.NEGATIVE)
searching_friend_keyboard.add_button(emoji.report, VkKeyboardColor.SECONDARY)
searching_friend_keyboard.add_button(emoji.back, VkKeyboardColor.PRIMARY)
searching_friend_keyboard = searching_friend_keyboard.get_keyboard()

chat_keyboard = VkKeyboard(one_time=False)
chat_keyboard.add_button(emoji.search, VkKeyboardColor.NEGATIVE)
chat_keyboard.add_button(emoji.report, VkKeyboardColor.SECONDARY)
chat_keyboard.add_button(emoji.back, VkKeyboardColor.PRIMARY)
chat_keyboard = chat_keyboard.get_keyboard()

