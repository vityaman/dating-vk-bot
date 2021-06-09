from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import res


begin_keyboard = VkKeyboard(one_time=False)
begin_keyboard.add_button("Begin", VkKeyboardColor.PRIMARY)
begin_keyboard = begin_keyboard.get_keyboard()

settings_keyboard = VkKeyboard(one_time=False)
settings_keyboard.add_button("Name", VkKeyboardColor.SECONDARY)
settings_keyboard.add_button("Age", VkKeyboardColor.SECONDARY)
settings_keyboard.add_line()
settings_keyboard.add_button("About", VkKeyboardColor.SECONDARY)
settings_keyboard.add_button("Interests", VkKeyboardColor.SECONDARY)
settings_keyboard.add_line()
settings_keyboard.add_button("Photo", VkKeyboardColor.SECONDARY)
settings_keyboard.add_line()
settings_keyboard.add_button("Save", VkKeyboardColor.NEGATIVE)
settings_keyboard = settings_keyboard.get_keyboard()

input_cancel_keyboard = VkKeyboard(one_time=False)
input_cancel_keyboard.add_button("Cancel", VkKeyboardColor.NEGATIVE)
input_cancel_keyboard = input_cancel_keyboard.get_keyboard()

main_menu_keyboard = VkKeyboard(one_time=False)
main_menu_keyboard.add_button(res.emoji.search, VkKeyboardColor.PRIMARY)
main_menu_keyboard.add_button(res.emoji.fax, VkKeyboardColor.PRIMARY)
main_menu_keyboard.add_button(res.emoji.settings, VkKeyboardColor.SECONDARY)
main_menu_keyboard = main_menu_keyboard.get_keyboard()

searching_friend_keyboard = VkKeyboard(one_time=False)
searching_friend_keyboard.add_button(res.emoji.like, VkKeyboardColor.POSITIVE)
searching_friend_keyboard.add_button(res.emoji.dislike, VkKeyboardColor.NEGATIVE)
searching_friend_keyboard.add_button(res.emoji.report, VkKeyboardColor.SECONDARY)
searching_friend_keyboard.add_button(res.emoji.back, VkKeyboardColor.PRIMARY)
searching_friend_keyboard = searching_friend_keyboard.get_keyboard()

chat_keyboard = VkKeyboard(one_time=False)
chat_keyboard.add_button(res.emoji.search, VkKeyboardColor.NEGATIVE)
chat_keyboard.add_button(res.emoji.report, VkKeyboardColor.SECONDARY)
chat_keyboard.add_button(res.emoji.back, VkKeyboardColor.PRIMARY)
chat_keyboard = chat_keyboard.get_keyboard()

