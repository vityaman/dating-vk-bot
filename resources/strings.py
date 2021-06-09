import config
import resources.emojis as emoji
import resources.languages as lang


if config.LANGUAGE == lang.ru:
    begin = \
        f"""Начать"""
    begin_hello = \
        f"""Добро пожаловать!
            Для начала зарегаем тебя.
            Вот настроечки! Заполни данные:"""
    begin_guide = \
        f"""О, сладкий!
            Ты тут впервые?
            Нажми "Начать", чтобы продолжить :)"""
    main_menu_guide = \
        f"""Ты в главном меню.
            Доступные функции:
            {emoji.search} Поиск (Начать искать друзей)
            {emoji.fax} Чат (Переписываться с рандомами)
            {emoji.settings} Настройки (Изменить свои данные)"""
    form_heading = \
        f"""| Ваш аккаунт |
            
            """
    main_menu_preparing_suggestions = \
        f"""Ищем вам друзей..."""
    main_menu_found = \
        f"""Готово! Найдено людей:"""
    main_menu_welcome_chat = \
        f"""Добро пожаловать в чат!
            Здесь ты можешь пообщаться.
            Нажми {emoji.search} чтобы найти диалог!"""
    searching_friend_exit = \
        f"""На сегодня все, больше пользователей нет!
            Добро пожаловать обратно в главное меню!"""
    searching_friend_look_next = \
        f"""Опа, смотри кого нашел:"""
    searching_friend_guide = \
        f"""Ты в разделе поиска друзей!
            Доступные функции:
            {emoji.like} Лайк (Лайкнуть человека)
            {emoji.dislike} Дальше (Получить еще одного)
            {emoji.report} Пожаловаться (Отправить жалобу)
            {emoji.back} Назад (Вернуться в главное мен)"""
    searching_friend_match_1 = \
        f"""Поздравляю!
            У вас взаимная лубов.
            Вот ссылочка на вконтактик:"""
    searching_friend_match_2 = \
        f"""Тили-тили тесто! поздравляю, боец!
            Наконец-то ты хоть кому-то приглянулся:"""
    searching_friend_match_motivation_1 = \
        f"""Приятного времяпрепровождения!"""
    searching_friend_match_motivation_2 = \
        f"""Не стесняйся!"""
    report_was_sent = \
        f"""Спасибки! Жалоба отправлена админу!"""
    chat_queue = \
        f"""Ты в очереди...
            подожди немножко..."""
    chat_found = \
        f"""Нашелся собеседник:"""
    chat_talk = \
        f"""Базарьте!"""
    chat_exit = \
        f"""Ясно. Пока!
            Увидимся"""
    chat_guide = \
        f"""Ты в разделе чата!
            Доступные функции:
            {emoji.search} Поиск (Искать беседу)
            {emoji.report} Пожаловаться (Отправить жалобу)
            {emoji.back} Назад (Вернуться в главное меню)"""
    chatting_exit = \
        f"""Добазарились спокойно, без лишних слов.
            Эх, хорошо побалакали... {emoji.sad}"""
    settings_guide = \
        f"""Ты в настройках, братанчик.
            Доступные функции:
            {emoji.smile} Имя (Ввести имя)
            {emoji.glasses} Возраст (Указать возраст)
            {emoji.talk} О себе (Написать о себе)
            {emoji.camera} Фото (Установить аву)
            {emoji.save} Сохранить (Сохранить изменения)"""
    name = "Имя"
    age = "Возраст"
    about = "О себе"
    interests = "Интересы"
    photo = "Фото"
    save = "Сохранить"
    cancel = "Отмена"
    settings_name = \
        f"""Как звать-то тебя, милаш?"""
    settings_age = \
        f"""И сколько же тебе лет?
            Чур не обманывать!"""
    settings_about = \
        f"""Ну давай, расскажи о себе!
            Мне, оч интересно, паравда..."""
    settings_interests = \
        f"""Чем ты интересуешься?
            Чтобы улучшить качество подбора друзей,
            Просто введи номера тэгов:
            """
    settings_photo = \
        f"""Все хотят тебя... увидеть!
            Да я знаю, что ты милашечка.
            Send photo pls!!"""
    accepted = "Принято!"
    settings_fill_all = \
        f"""Все поля должны быть заполнены"""
    settings_return = \
        f"""Вернул тебя назад."""
    settings_invalid_input = \
        f"""Это введеные данные инвалид или ты?"""
    settings_ok_name = \
        f"""Приятно познакомиться!"""
    settings_ok_age = \
        f"""О, круть! В твоем возрасте самое время искать себе лубов!
            Без этого никак..."""
    settings_ok_about = \
        f"""Ну, ты крутой чел, да."""
    settings_ok_interests = \
        f"""Интересы приняты!"""
    settings_ok_photo = \
        f"""Ты... т... т... такая красивая..., 
            ой, ладно... я пошел... {emoji.shyhands}"""

elif config.LANGUAGE == lang.eng:
    begin = \
        f"""Begin"""
    begin_hello = \
        f"""Welcome!
            We'll register you first.
            Here are the settings. Fill the from:"""
    begin_guide = \
        f"""Oh, hello, honey!
            Are you for the first time here?
            Press "Begin" to continue :)"""
    main_menu_guide = \
        f"""You are in the main menu.
            Available functions:
            {emoji.search} Search (Start search your love)
            {emoji.fax} Chat (Chatting with randoms)
            {emoji.settings} Settings (Edit your data)"""
    form_heading = \
        f"""| Your account |"""
    main_menu_preparing_suggestions = \
        f"""Preparing suggestions for you..."""
    main_menu_found = \
        f"""Ready! Found users count:"""
    main_menu_welcome_chat = \
        f"""Welcome to chat!
            Here you can find conservations.
            Press {emoji.search} to find chat!"""
    searching_friend_exit = \
        f"""That's all for this session!
            Welcome back to main menu!"""
    searching_friend_look_next = \
        f"""Oh, look what a cool person:"""
    searching_friend_guide = \
        f"""You are in searching friends section!
            Available functions:
            {emoji.like} Like (Like person)
            {emoji.dislike} Next (Get next)
            {emoji.report} Report (Send a complaint)
            {emoji.back} Back (Back to the main menu)"""
    searching_friend_match_1 = \
        f"""Congratulations!
            This is the match.
            Here is the link to VK page:"""
    searching_friend_match_2 = \
        f"""Congratulations!
            You have the match:"""
    searching_friend_match_motivation_1 = \
        f"""Good online time spending!"""
    searching_friend_match_motivation_2 = \
        f"""Don't be shy!"""
    report_was_sent = \
        f"""Thanks! Report was sent to admin!"""
    chat_queue = \
        f"""You are in queue...
            Please, wait..."""
    chat_found = \
        f"""Chat has been found:"""
    chat_talk = \
        f"""Talk!"""
    chat_exit = \
        f"""OK, goodbye!
            See ya later..."""
    chat_guide = \
        f"""You are in the chat section!
            Available functions:
            {emoji.search} Search (Search conservation)
            {emoji.report} Report (Report user)
            {emoji.back} Back (Back to main menu)"""
    chatting_exit = \
        f"""Conversation ended.
            It was nice... {emoji.sad}"""
    settings_guide = \
        f"""You are in settings menu.
            Available commands:
            {emoji.smile} Name (Enter your name)
            {emoji.glasses} Age (Enter your age)
            {emoji.talk} About (Write about you)
            {emoji.camera} Photo (Set avatar photo)
            {emoji.save} Save (Save changes)"""
    name = "Name"
    age = "Age"
    about = "Bio"
    interests = "Interests"
    photo = "Photo"
    save = "Save"
    cancel = "Cancel"
    settings_name = \
        f"""What is your name?"""
    settings_age = \
        f"""How old are you?
            Just don't cheat, please..."""
    settings_about = \
        f"""Tell me about yourself!
            I'm really interested in it..."""
    settings_interests = \
        f"""Choice interests tags for your profile
            It will improve your suggestions!
            Just type numbers of tags:
        """
    settings_photo = \
        f"""Everyone want to see you!
            I'm sure you're beauty.
            Send photo pls!!"""
    accepted = "Accepted!"
    settings_fill_all = \
        f"""You must fill all fields!"""
    settings_return = \
        f"""Return you back."""
    settings_invalid_input = \
        f"""Invalid Input!"""
    settings_ok_name = \
        f"""Nice to meet you!"""
    settings_ok_age = \
        f"""Oh, nice! It's time to find love!
            In yours age it's necessary!"""
    settings_ok_about = \
        f"""Ohh, yeah, dude, I knew, that you are cool person!"""
    settings_ok_interests = \
        f"""Interests accepted!"""
    settings_ok_photo = \
        f"""You... so cute... oh, sorry, 
            I have to go... {emoji.shyhands}"""
