import random

import vk_api
import vk_api.bot_longpoll
import token_1 as token
group_id = '201019551'

class VkBot:

    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token.token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = vk_api.bot_longpoll.VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            print('Событие - ')
            try:
                self.on_event(event)
            except Exception as exc:
                print('ошибка', exc)

    def on_event(self, event):
        if event.t == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
            print(event.message.text)
            self.api.messages.send(
                message='Сам такой!',
                random_id=random.randint(0, 100000),
                peer_id=event.message.peer_id,
            )
        else:
            print('Я так не умею!', event.t)

    def message(self):
        pass


if __name__ == '__main__':
    bot = VkBot(group_id, token)
    bot.run()
