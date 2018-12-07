#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests

class Telegram():
    def __init__(self, token):
        self.token = token

    def send_simple_message(self, chat_id, message, parse_mode='HTML'):
        url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, 'sendMessage')
        payload = {'chat_id': chat_id,
                   'text': message,
                   'parse_mode': parse_mode}
        print('url', url)
        r = requests.post(url, data=payload)
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json())

    def kick_member(self, chat_id, user_id):
        url = 'https://api.telegram.org/bot{0}/{1}'.format(self.token, 'kickChatMember')
        payload = {'chat_id': chat_id,
                   'user_id': user_id}
        print('url', url)
        r = requests.post(url, data=payload)
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        print(r.text)
        print(r.json())
