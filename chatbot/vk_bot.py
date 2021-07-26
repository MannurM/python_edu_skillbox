import random
import logging
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import token_1 as token

group_id = '201019551'
log = logging.getLogger("bot")
stream_hendler = logging.StreamHandler()
stream_hendler.setFormatter(logging.Formatter('%(levelname)s % (message)s'))
log.addHandler(stream_hendler)

file_handler = logging.FileHandler('bot.log')

file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s % (message)s'))
log.addHandler(file_handler)

log.setLevel(logging.DEBUG)
stream_hendler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL


class VkBot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token.token
        self.vk = vk_api.VkApi(token=self.token)
        self.long_poller = VkBotLongPoll(self.vk, self.group_id)
        self.api = self.vk.get_api()

    def run(self):
        for event in self.long_poller.listen():
            try:
                self.on_event(event)
            except Exception:
                log.exception('Ошибка в обработке события')

    def on_event(self, event):
        if event.type == VkBotEventType.MESSAGE_NEW:
            log.info('Возвращаем сообщение')
            self.api.messages.send(
                message='Приветствую Вас, Землянин!!',
                random_id=random.randint(0, 100000),
                peer_id=event.message.peer_id,
            )
        else:
            log.debug('Я так не умею!')

    def message(self):
        pass


if __name__ == '__main__':
    bot = VkBot(group_id, token)
    bot.run()
