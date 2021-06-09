from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from bot.dating_bot import DatingBot
from event_handlers.message_handling.user_message_handler import UserMessageHandler
from vk_tools.vkapi_provider import VKAPIProvider
import config as cfg

# TODO: it makes me fear:
from event_handlers.message_handling.user_environments import *


if __name__ == '__main__':
    bot = DatingBot(cfg.VK_GROUP_ID,  VKAPIProvider(cfg.VK_ACCESS_TOKEN))

    UserMessageHandler.initialize()

    longpool = VkBotLongPoll(bot.vk.vk, bot.group_id)
    for event in longpool.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.object.peer_id == cfg.VK_ADMIN_CHAT_ID:
                if event.object.from_id == cfg.VK_ADMIN_ID:
                    # TODO: admin_message_handler.handle(event.object)
                    pass
            else:
                UserMessageHandler.handle(bot, event.object)
