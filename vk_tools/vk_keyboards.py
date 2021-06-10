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

admin_panel_keyboard = VkKeyboard(one_time=False)
admin_panel_keyboard.add_button(emoji.stats, VkKeyboardColor.POSITIVE)
admin_panel_keyboard.add_button(emoji.police, VkKeyboardColor.NEGATIVE)
admin_panel_keyboard.add_button(emoji.notify, VkKeyboardColor.PRIMARY)
admin_panel_keyboard.add_button(emoji.settings, VkKeyboardColor.SECONDARY)
admin_panel_keyboard = admin_panel_keyboard.get_keyboard()

consider_report_keyboard = VkKeyboard(one_time=False)
consider_report_keyboard.add_button(emoji.police, VkKeyboardColor.POSITIVE)
consider_report_keyboard.add_button('Sender', VkKeyboardColor.SECONDARY)
consider_report_keyboard.add_button('Criminal', VkKeyboardColor.PRIMARY)
consider_report_keyboard.add_button(emoji.back, VkKeyboardColor.NEGATIVE)
consider_report_keyboard = consider_report_keyboard.get_keyboard()

consider_user_keyboard = VkKeyboard(one_time=False)
consider_user_keyboard.add_button(emoji.back, VkKeyboardColor.SECONDARY)
consider_user_keyboard = consider_user_keyboard.get_keyboard()
