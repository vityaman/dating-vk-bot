import os


# secret key for using vk_api
VK_ACCESS_TOKEN = str(os.environ['VK_ACCESS_TOKEN'])
# group where bot is working
VK_GROUP_ID = int(os.environ['VK_GROUP_ID'])
# chat where will send messages-notifications
VK_ADMIN_CHAT_ID = int(os.environ['VK_ADMIN_CHAT_ID'])
# admin id
VK_ADMIN_ID = int(os.environ['VK_ADMIN_ID'])

# database url
DATABASE_URL = str(os.environ['DATABASE_URL'])
