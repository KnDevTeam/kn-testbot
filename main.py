"""
Starting November 28, 2022, free Heroku Dynos, Redis and PostgreSQL will no longer be available
https://blog.heroku.com/next-chapter
"""

import os
from time import sleep
import telebot
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)


"""
@bot.message_handler(content_types=["new_chat_members"])
def foo(message):
    bot.reply_to(message, "welcome")
"""


@bot.message_handler(content_types=["new_chat_members"])
def foo(message):
    bot.reply_to(message, "Привет, добро пожаловать!\nЯ просто тупой тестовый бот.\nНу раз уж ты здесь, то про Крым уже не буду спрашивать... 🤭\n\n© KN-IT Team")



# Handler for start command
@bot.message_handler(commands=['start'])
def start(message):

    username = message.from_user.username
    msg_start = bot.reply_to(message, f"Привет: {username}!\nЯ просто тестовый бот,\nРазработан отделом KN - IT.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for help command
HELP = '''
Что я могу:
⚡️ /help: Справка по командам.
⚡️ /add: Добавить пользователя в группу по user_id. [доступно только адм.]
⚡️ /all: Список всех пользователей группы. [доступно только адм.]
⚡️ /call: Отправить всем уведомление.
⚡️ /call N: Отправить всем уведомление N раз.
⚡️ /callu @User_X: Отправить уведомление пользователю X.
⚡️ /callu @User_X N: Отправить уведомление юзеру X, N раз.
⚡️ /del @User_X: Удалить из группы пользователя X по user_id. [доступно только адм.]
⚡️ /getid: Узнать свой user_id, либо ответь на сообщение указав команду, чтоб получить user_id пользователя.
На данном этапе, чтоб не флудить. Я удалю сообщение через 15 секунд!
©Powered by KN-IT Team
'''
@bot.message_handler(commands=['help'])
def help(message):

    msg_help = bot.reply_to(message, HELP, disable_notification=True)
    sleep(15)
    bot.delete_message(message.chat.id, msg_help.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for all command
@bot.message_handler(commands=['all'])
def start(message):

    msg_start = bot.reply_to(message, f"Эта команда выведет список участников, данного чата.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for call command
@bot.message_handler(commands=['call'])
def start(message):

    msg_start = bot.reply_to(message, f"Эта команда по дефолту вышлит оповещание, всем участникам данного чата.\nЕсли добален параметр N раз, то с задержкой в 10 сек. вышлет N раз\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for callu command
@bot.message_handler(commands=['callu'])
def start(message):

    msg_start = bot.reply_to(message, f"Эта команда вышлит оповещание, определённому участнику данного чата.\nЕсли добален параметр N раз, то с задержкой в 10 сек. вышлет N раз\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for add command
@bot.message_handler(commands=['add'])
def start(message):

    msg_start = bot.reply_to(message, "Эта команда добавит определённого участника в список, данного чата.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for del command
@bot.message_handler(commands=['del'])
def start(message):

    msg_start = bot.reply_to(message, "Эта команда удалит определённого участника из списка, данного чата.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for getid command
@bot.message_handler(commands=['getid'])
def start(message):

    name = message.from_user
    if name.first_name == None:
        name.first_name = "Не указанно"
    if name.last_name == None:
        name.last_name = "Не указанно"
    if name.username == None:
        name.username = "Не указанно"
    if name.is_premium == False:
        name.is_premium = "Не премиум"
    else:
        name.is_premium = "Премиум"

    msg_id = bot.reply_to(message, f"Имя: {name.first_name}\nФамилия: {name.last_name}\nИмя пользователя: @{name.username}\nuser_id: {name.id}\nЯзык: {name.language_code}\nПремиум аккаунт: {name.is_premium}\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_id.message_id)
    bot.delete_message(message.chat.id, message.message_id)




@server.route(f'/{BOT_TOKEN}', methods=['POST'])
def redirect_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url=APP_URL)
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))