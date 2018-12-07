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

import logging
import subprocess
import os
import time
from flask import Flask, request, abort
from dobot.telegramapi import Telegram

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('mumblebot.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

app = Flask(__name__)

@app.route("/mumblebot/")
def hello():
    return "<h1>¿Que miras aquí?, ¡Mameluco!</h1>"

@app.route("/mumblebot/test/")
def hello2():
    return "<h1>¿Que miras aquí, también?, ¡Mameluco!</h1>"

@app.route("/mumblebot/998d4bcc-2798-4ca5-9be7-48588f0573c4", methods=['POST', 'GET'])
def actions():
    if request.method == 'POST':
       update = request.json
        logger.info(update)
        logger.info(os.system('echo $USER'))
        if 'message' in update and 'text' in update['message']:
            telegram = Telegram(app.token)
            if update['message']['text'] == '/start':
                os.system('/usr/bin/sudo /home/user/mumble_scripts/start.sh')
                telegram.send_simple_message(update['message']['chat']['id'], 'Please **wait** three seconds', parse_mode='Markdown')
                time.sleep(3)
                msg = subprocess.Popen(['/usr/bin/sudo', '/home/user/mumble_scripts/info.sh'], stdout=subprocess.PIPE).stdout.read()
                telegram.send_simple_message(update['message']['chat']['id'], msg, parse_mode='Markdown')
            elif update['message']['text'] == '/stop':
                os.system('/usr/bin/sudo /home/user/mumble_scripts/stop.sh')
                telegram.send_simple_message(update['message']['chat']['id'], 'Please **wait** three seconds', parse_mode='Markdown')
                time.sleep(3)
                msg = subprocess.Popen(['/usr/bin/sudo', '/home/user/mumble_scripts/info.sh'], stdout=subprocess.PIPE).stdout.read()
                telegram.send_simple_message(update['message']['chat']['id'], msg, parse_mode='Markdown')
            elif update['message']['text'] == '/info':
                msg = subprocess.Popen(['/usr/bin/sudo', '/home/user/mumble_scripts/info.sh'], stdout=subprocess.PIPE).stdout.read()
                telegram.send_simple_message(update['message']['chat']['id'], msg, parse_mode='Markdown')
            elif update['message']['text'] == '/help':
                msg  = 'This **bot** starts and stops a Mumble Server\n\n'
                msg += '**Use this commands**:\n\n'
                msg += '`/help` - **Show** this help\n'
                msg += '`/info` - Get the **status** of the Mumble Server\n'
                msg += '`/start` - **Starts** the Mumble Server\n'
                msg += '`/stop` - **Stops** the Mumble Server'
                telegram.send_simple_message(update['message']['chat']['id'], msg, parse_mode='Markdown')
        return 'post', 200
    elif request.method == 'GET':
        print('Hola 2')
        return 'get', 200
    else:
        abort(400)


if __name__ == "__main__":
    print(1)
    app.run(host='0.0.0.0')
