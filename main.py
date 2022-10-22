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
    username = message.from_user.username
    bot.reply_to(message, f"Привет, {username.first_name}, {username.last_name} добро пожаловать!\nЯ просто бот и просто слежу за порядком.\nНадеюсь про Крым нет необходимости спрашивать? 🤭\nТы можешь посмотреть доступные команды /help\n\n© KN-IT Team")



# Handler for start command
@bot.message_handler(commands=['start'])
def start(message):

    username = message.from_user.username
    msg_start = bot.reply_to(message, f"Привет: {username.first_name} {username.last_name}!\nЯ просто тестовый бот,\nРазработан отделом KN - IT.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for rules command
RULES = '''
ПРАВИЛА ЧАТА В КИЛЛНЕТ !!!

Никаких оскорблений, объявлений купли / продажи или предложений каких либо сервисов. Никаких реклам своих каналов и других источников.

Также, хочу напомнить, что запрещенно оставлять ссылки на внешние источники, темболее с отработкой в JS, либо html.
Это в целях безопастности всех участников. В данном чате находятся люди далёкие от IT сферы.
Ссылки разрешенны на крупные и известные сайты с preview. Если они конечно по теме.

За портянки и постоянные перепосты новостей - будет наложен мут, вплоть до исключения из группы.

Относитесь друг к другу с уважением! Если есть проблеммы, пишите модераторам. Вы все люди и у вас есть правила приличия и этикет !

СОБЛЮДАЙТЕ ИХ !

Здесь Killnet детка - самая мощная и опасная группировка РФ.
❤🇷🇺❤

© KN-IT Team
'''
@bot.message_handler(commands=['rules'])
def rules(message):

    msg_rules = bot.reply_to(message, RULES, disable_notification=True)
    sleep(45)
    bot.delete_message(message.chat.id, msg_rules.message_id)
    bot.delete_message(message.chat.id, message.message_id)

# Handler for help command
HELP = '''
Команды общего доступа

/help - Эта команда вызывает меню помоши
/contact - Эта команда покажет единственную официальную связь с KILLNET
/donate - Эта команда позволит увидеть как можно нас поддержать
/rules - Эта команда укажет на правила в чате

© KN-IT Team
'''
@bot.message_handler(commands=['help'])
def help(message):

    msg_help = bot.reply_to(message, HELP, disable_notification=True)
    sleep(30)
    bot.delete_message(message.chat.id, msg_help.message_id)
    bot.delete_message(message.chat.id, message.message_id)

# Handler for help command
CONTACT = '''

ВНИМАНИЕ!!! 

ВСЕ НЕЙМЫ НИЖЕ, ЯВЛЯЮТСЯ ОФИЦИАЛЬНЫМИ КОНТАКТАМИ KILLNET! 

ПО ВСЕМ ВОПРОСАМ и ДЛЯ СМИ
 @killnet_support
СЛУЖБА БЕЗОПАСНОСТИ
 @Alpham65bot
МИНИСТР ИНОСТРАННЫХ ДЕЛ
 @kill_here

Официальный:
 @killmilk_rus
Писарь из Штаба (резерв) 
 @killnet_mirror

 Killmilk
@killmilk_russ

 ЕСЛИ С ВАМИ СВЯЗАЛИСЬ ОТ НАШЕГО ИМЕНИ, И ПРЕДЛОЖИЛИ СОТРУДНИЧЕСТВО - ШЛИТЕ НА#УЙ! 
 У НАС НЕТ ТЕХНИЧЕСКИХ ПРОБЛЕМ И СБОЕВ В РАБОТЕ! ВСЕ КОНТАКТЫ ВЫШЕ, ДОСТУПНЫ 24/7

🇷🇺СЛАВА РОССИИ


© KN-IT Team
'''
@bot.message_handler(commands=['contact'])
def contact(message):

    msg_contact = bot.reply_to(message, CONTACT, disable_notification=True)
    sleep(60)
    bot.delete_message(message.chat.id, msg_contact.message_id)
    bot.delete_message(message.chat.id, message.message_id)

# Handler for help command
DONATE = '''

🔥СБЕРБАНК
4279380693810329

🔥КИВИ БАНК
4890494798144549

🔥BTC
bc1qvqvppw5gmmdnsq7xakg52jthcj3axx6guv4n24

🔥ETH
0xedA9832a67711f98E128BCB8F21544dfc273C6B1

🔥USDT TRC20
TSQGBoX32EkkmpFDg1gcm6QwiHeoDrACNx

🔥XMR MONERO
42exW4JPKnm2mgb1vXC8Q66rvsWhx9EVT42UExV3sjvfFHgQXeXzb7act9YNZRepEYJHsFVzFnbCe5jm2DfKGkwwVNz9dqs

❕Если Вам нужен другой адрес, пожалуйста напишите @killnet_support


🟢 В соответствии с положениями пункта 18.1 ст. 217 Налогового Кодекса РФ, освобождаются от обложения налогом на доходы физических лиц, доходы физических лиц в денежной и натуральной формах, получаемые ими от физических лиц в порядке дарения.


© KN-IT Team
'''
@bot.message_handler(commands=['donate'])
def donate(message):

    msg_donate = bot.reply_to(message, DONATE, disable_notification=True)
    sleep(60)
    bot.delete_message(message.chat.id, msg_donate.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for all command
@bot.message_handler(commands=['allgaghrhreheag'])
def start(message):

    msg_start = bot.reply_to(message, f"Эта команда выведет список участников, данного чата.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for call command
@bot.message_handler(commands=['callggaeah'])
def start(message):

    msg_start = bot.reply_to(message, f"Эта команда по дефолту вышлит оповещание, всем участникам данного чата.\nЕсли добален параметр N раз, то с задержкой в 10 сек. вышлет N раз\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for callu command
@bot.message_handler(commands=['callurewehyehyweh'])
def start(message):

    msg_start = bot.reply_to(message, f"Эта команда вышлит оповещание, определённому участнику данного чата.\nЕсли добален параметр N раз, то с задержкой в 10 сек. вышлет N раз\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for add command
@bot.message_handler(commands=['addehehewhew'])
def start(message):

    msg_start = bot.reply_to(message, "Эта команда добавит определённого участника в список, данного чата.\n\nЯ сам удалю сообщения через 7 секунд, чтоб не флудить\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for del command
@bot.message_handler(commands=['delerhehewhrwehe'])
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