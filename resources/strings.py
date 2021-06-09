import config
import resources.emojis as emoji
import resources.languages as lang

if config.LANGUAGE == lang.ru:
    begin = "Начать"
    begin_hello = \
        ("Добро пожаловать!\n"
         "Для начала зарегаем тебя.\n"
         "Вот настроечки! Заполни данные:")
    begin_guide = \
        ("О, сладкий!\n"
         "Ты тут впервые?\n"
         "Нажми \"Начать\", чтобы продолжить :)")
    main_menu_guide = \
        (f"Ты в главном меню.\n"
         f"Доступные функции:\n"
         f"{emoji.search} Поиск (Начать искать друзей)\n"
         f"{emoji.fax} Чат (Переписываться с рандомами)\n"
         f"{emoji.settings} Настройки (Изменить свои данные)")
    form_heading = \
        (f"| Ваш аккаунт |\n\n")
    main_menu_preparing_suggestions = \
        f"Ищем вам друзей..."
    main_menu_found = \
        f"Готово! Найдено людей:"
    main_menu_welcome_chat = \
        (f"Добро пожаловать в чат!\n"
         f"Здесь ты можешь пообщаться.\n"
         f"Нажми {emoji.search} чтобы найти диалог!")
    searching_friend_exit = \
        (f"На сегодня все, больше пользователей нет!\n"
         f"Добро пожаловать обратно в главное меню!")
    searching_friend_look_next = \
        f"Опа, смотри кого нашел:"
    searching_friend_guide = \
        (f"Ты в разделе поиска друзей!\n"
         f"Доступные функции:\n"
         f"{emoji.like} Лайк (Лайкнуть человека)\n"
         f"{emoji.dislike} Дальше (Получить еще одного)\n"
         f"{emoji.report} Пожаловаться (Отправить жалобу)\n"
         f"{emoji.back} Назад (Вернуться в главное мен)")
    searching_friend_match_1 = \
        (f"Поздравляю!\n"
         f"У вас взаимная лубов.\n"
         f"Вот ссылочка на вконтактик:")
    searching_friend_match_2 = \
        (f"Тили-тили тесто! поздравляю, боец!\n"
         f"Наконец-то ты хоть кому-то приглянулся:")
    searching_friend_match_motivation_1 = \
        f"Приятного времяпрепровождения!"
    searching_friend_match_motivation_2 = \
        f"Не стесняйся!"
    report_was_sent = \
        f"Спасибки! Жалоба отправлена админу!"
    chat_queue = \
        (f"Ты в очереди...\n"
         f"подожди немножко...")
    chat_found = \
        f"Нашелся собеседник:"
    chat_talk = \
        f"Базарьте!"
    chat_exit = \
        (f"Ясно. Пока!\n"
         f"Увидимся")
    chat_guide = \
        (f"Ты в разделе чата!\n"
         f"Доступные функции:\n"
         f"{emoji.search} Поиск (Искать беседу)\n"
         f"{emoji.report} Пожаловаться (Отправить жалобу)\n"
         f"{emoji.back} Назад (Вернуться в главное меню)")
    chatting_exit = \
        (f"Добазарились спокойно, без лишних слов.\n"
         f"Эх, хорошо побалакали... {emoji.sad}")
    settings_guide = \
        (f"Ты в настройках, братанчик.\n"
         f"Доступные функции:\n"
         f"{emoji.smile} Имя (Ввести имя)\n"
         f"{emoji.glasses} Возраст (Указать возраст)\n"
         f"{emoji.talk} О себе (Написать о себе)\n"
         f"{emoji.camera} Фото (Установить аву)\n"
         f"{emoji.save} Сохранить (Сохранить изменения)")
    name = "Имя"
    age = "Возраст"
    about = "О себе"
    interests = "Интересы"
    photo = "Фото"
    save = "Сохранить"
    cancel = "Отмена"
    settings_name = \
        f"Как звать-то тебя, милаш?"
    settings_age = \
        (f"И сколько же тебе лет?\n"
         f"Чур не обманывать!")
    settings_about = \
        (f"Ну давай, расскажи о себе!\n"
         f"Мне, оч интересно, паравда...")
    settings_interests = \
        (f"Чем ты интересуешься?\n"
         f"Чтобы улучшить качество подбора друзей,\n"
         f"Просто введи номера тэгов:\n\n")
    settings_photo = \
        (f"Все хотят тебя... увидеть!\n"
         f"Да я знаю, что ты милашечка.\n"
         f"Send photo pls!!")
    accepted = "Принято!"
    settings_fill_all = \
        f"Все поля должны быть заполнены"
    settings_return = \
        f"Вернул тебя назад."
    settings_invalid_input = \
        f"Это введеные данные инвалид или ты?"
    settings_ok_name = \
        f"Приятно познакомиться!"
    settings_ok_age = \
        (f"О, круть! В твоем возрасте самое время искать себе лубов!\n"
         f"Без этого никак...")
    settings_ok_about = \
        f"Ну, ты крутой чел, да."
    settings_ok_interests = \
        f"Интересы приняты!"
    settings_ok_photo = \
        (f"Ты... т... т... такая красивая..., \n"
         f"ой, ладно... я пошел... {emoji.shyhands}")

elif config.LANGUAGE == lang.eng:
    begin = \
        f"Begin"
    begin_hello = \
        (f"Welcome!\n"
         f"We'll register you first.\n"
         f"Here are the settings. Fill the from:")
    begin_guide = \
        (f"Oh, hello, honey!\n"
         f"Are you for the first time here?\n"
         f"Press \"Begin\" to continue :)")
    main_menu_guide = \
        (f"You are in the main menu.\n"
         f"Available functions:\n"
         f"{emoji.search} Search (Start search your love)\n"
         f"{emoji.fax} Chat (Chatting with randoms)\n"
         f"{emoji.settings} Settings (Edit your data)")
    form_heading = \
        f"| Your account |"
    main_menu_preparing_suggestions = \
        f"Preparing suggestions for you..."
    main_menu_found = \
        f"Ready! Found users count:"
    main_menu_welcome_chat = \
        (f"Welcome to chat!\n"
         f"Here you can find conservations.\n"
         f"Press {emoji.search} to find chat!")
    searching_friend_exit = \
        (f"That's all for this session!\n"
         f"Welcome back to main menu!")
    searching_friend_look_next = \
        f"Oh, look what a cool person:"
    searching_friend_guide = \
        (f"You are in searching friends section!\n"
         f"Available functions:\n"
         f"{emoji.like} Like (Like person)\n"
         f"{emoji.dislike} Next (Get next)\n"
         f"{emoji.report} Report (Send a complaint)\n"
         f"{emoji.back} Back (Back to the main menu)")
    searching_friend_match_1 = \
        (f"Congratulations!\n"
         f"This is the match.\n"
         f"Here is the link to VK page:")
    searching_friend_match_2 = \
        (f"Congratulations!\n"
         f"You have the match:")
    searching_friend_match_motivation_1 = \
        f"Good online time spending!"
    searching_friend_match_motivation_2 = \
        f"Don't be shy!"
    report_was_sent = \
        f"Thanks! Report was sent to admin!"
    chat_queue = \
        (f"You are in queue...\n"
         f"Please, wait...")
    chat_found = \
        f"Chat has been found:"
    chat_talk = \
        f"Talk!"
    chat_exit = \
        (f"OK, goodbye!\n"
         f"See ya later...")
    chat_guide = \
        (f"You are in the chat section!\n"
         f"Available functions:\n"
         f"{emoji.search} Search (Search conservation)\n"
         f"{emoji.report} Report (Report user)\n"
         f"{emoji.back} Back (Back to main menu)")
    chatting_exit = \
        (f"Conversation ended.\n"
         f"It was nice... {emoji.sad}")
    settings_guide = \
        (f"You are in settings menu.\n"
         f"Available commands:\n"
         f"{emoji.smile} Name (Enter your name)\n"
         f"{emoji.glasses} Age (Enter your age)\n"
         f"{emoji.talk} About (Write about you)\n"
         f"{emoji.camera} Photo (Set avatar photo)\n"
         f"{emoji.save} Save (Save changes)")
    name = "Name"
    age = "Age"
    about = "Bio"
    interests = "Interests"
    photo = "Photo"
    save = "Save"
    cancel = "Cancel"
    settings_name = \
        f"What is your name?"
    settings_age = \
        (f"How old are you?\n"
         f"Just don't cheat, please...")
    settings_about = \
        (f"Tell me about yourself!\n"
         f"I'm really interested in it...")
    settings_interests = \
        (f"Choice interests tags for your profile\n"
         f"It will improve your suggestions!\n"
         f"Just type numbers of tags:\n\n")
    settings_photo = \
        (f"Everyone want to see you!\n"
         f"I'm sure you're beauty.\n"
         f"Send photo pls!!")
    accepted = "Accepted!"
    settings_fill_all = \
        f"You must fill all fields!"
    settings_return = \
        f"Return you back."
    settings_invalid_input = \
        f"Invalid Input!"
    settings_ok_name = \
        f"Nice to meet you!"
    settings_ok_age = \
        (f"Oh, nice! It's time to find love!\n"
         f"In yours age it's necessary!")
    settings_ok_about = \
        f"Ohh, yeah, dude, I knew, that you are cool person!"
    settings_ok_interests = \
        f"Interests accepted!"
    settings_ok_photo = \
        (f"You... so cute... oh, sorry, \n"
         f"I have to go... {emoji.shyhands}")
