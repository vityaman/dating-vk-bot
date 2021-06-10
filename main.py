from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot.dating_bot import DatingBot
from event_handlers.message_handling.admin_message_handler import *
from event_handlers.message_handling.user_message_handler import *
from vk_tools.vkapi_provider import VKAPIProvider
import config as cfg


if __name__ == '__main__':
    bot = DatingBot(cfg.VK_GROUP_ID,  VKAPIProvider(cfg.VK_ACCESS_TOKEN))

    UserMessageHandler.initialize()
    AdminMessageHandler.initialize()

    longpool = VkBotLongPoll(bot.vk.vk, bot.group_id)
    try:
        for event in longpool.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.object.peer_id == cfg.VK_ADMIN_CHAT_ID:
                    if event.object.from_id == cfg.VK_ADMIN_ID:
                        AdminMessageHandler.handle(bot, event.object)
                else:
                    UserMessageHandler.handle(bot, event.object)
    finally:
        bot.db.close()
