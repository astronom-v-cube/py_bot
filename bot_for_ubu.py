#!/usr/bin/env python

import requests
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from my_token import main_token

def sender(id, text):
    vk_session.method ('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0})

vk_session = vk_api.VkApi(token = main_token, api_version = 5.95)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:

                msg = event.text
                id = event.user_id

                if msg == 'Привет' or 'привет' or 'Hello' or 'hello'  or 'Hi'  or 'Start':
                    sender(id, 'И тебе привет!')
