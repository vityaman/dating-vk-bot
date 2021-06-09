import requests
import vk_api

from random import randint


class VKAPIProvider:
    def __init__(self, vk_access_token):
        # vk session
        self.vk = vk_api.VkApi(token=vk_access_token)

    def send_message(self, peer, text, attachments=(), keyboard=''):
        self.vk.method('messages.send', {
            'peer_id': peer,
            'message': text,
            'keyboard': keyboard,
            'attachment': str(attachments)[1:-1].replace("'", ""),
            'random_id': randint(0, 999999)
        })

    def get_conversation_members(self, conversation, fields=()):
        return self.vk.method('messages.getConversationMembers', {
            'peer_id': conversation,
            'fields': str(fields)[1:-1]
        })['items']

    def get_users(self, users, fields=()):
        return self.vk.method('users.get', {
            'user_ids': str(users)[1:-1],
            'fields': str(fields)[1:-1]
        })

    def get_group_members(self, group_id, fields=()):
        return self.vk.method('groups.getMembers', {
            'group_id': group_id,
            'fields': str(fields)[1:-1]
        })['items']

    def is_group_members(self, group_id, users):
        return self.vk.method('groups.isMember', {
            'group_ud': group_id,
            'user_ids': str(users)[1:-1]
        })

    def save_photo_from_url(self, url: str) -> str:
        upload_server = self.vk.method("photos.getMessagesUploadServer")

        open("temp.jpg", "bw").write(requests.get(url).content)
        photo = requests.post(upload_server['upload_url'],
                              files={'photo': open("temp.jpg", "br")}).json()
        photo = self.vk.method('photos.saveMessagesPhoto', {
            'photo': photo['photo'],
            'server': photo['server'],
            'hash': photo['hash']})[0]
        return f"photo{photo['owner_id']}_{photo['id']}"
