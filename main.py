"""
Starting November 28, 2022, free Heroku Dynos, Redis and PostgreSQL will no longer be available
https://blog.heroku.com/next-chapter
"""

import os
from time import sleep
import telebot
from telebot import types, util
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

# SimpleCustomFilter is for boolean values, such as is_admin=True
class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']


#Command ban code
@bot.message_handler(is_admin = True, commands=['ban', 'бан'])
def getusers(message):
    if not message.reply_to_message:
        bot.reply_to(message, "🙄 Ошибка!\nНеобходимо ответить на сообщение. 😏\n\n© KN-IT Team")
        return
    
    # Admins cannot be restricted
    user = bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status in ['administrator','creator']
    if user:
        bot.reply_to(message, "Ты чего это? 🤦‍♂\nАдмин состав нельзя банить... 😂\n\n© KN-IT Team")
        return


    name = message.reply_to_message.from_user
    if name.first_name == None:
        name.first_name = "\"Невидимка\""
    if name.last_name == None:
        name.last_name = ""
    bot.send_message(message.chat.id, f"🤖 Упс... \n{name.first_name} {name.last_name}, выхватил БАН 🤭\n\n© KN-IT Team")
    bot.delete_message(message.chat.id, message.message_id)  # remove admin message
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    #bot.delete_message(message.reply_to_message.message_id, message.reply_to_message.from_user.id)  # remove all messages from baned user
    #bot.send_message(message.chat.id, "🤖 Упс... \nКто-то выхватил БАН 🤭\n\n© KN-IT Team")


@bot.message_handler(is_admin = False, commands=['ban', 'бан'])
def getusers(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Вау!!\nТы знаешь волшебное слово...\nАккуратней с такой игрушкой! 🤡\n\n© KN-IT Team")
        return

    bot.reply_to(message, "🤔 Хммм забанить да?\nЯ сейчас тебе бан выпишу... 🤧\n\n© KN-IT Team")

'''
@bot.message_handler(content_types=["new_chat_members"])
def welcome(message):
    name = message.from_user
    if name.first_name == None:
        name.first_name = ""
    if name.last_name == None:
        name.last_name = ""
    bot.reply_to(message, f"Привет, {name.first_name}, {name.last_name}\nПравила чата /rules\nОстальные доступные команды /help\n\n© KN-IT Team")
'''


# this handler deletes service messages
#@bot.message_handler(content_types=util.content_type_service)
@bot.message_handler(content_types=["new_chat_members"])
def delall(message: types.Message):
    bot.delete_message(message.chat.id,message.message_id)


# Handler for start command
@bot.message_handler(commands=['start', 'старт'])
def start(message):

    username = message.from_user
    msg_start = bot.reply_to(message, f"Привет: {username.first_name} {username.last_name} :)\nЯ просто тестовый бот\nРазработан отделом KN - IT.\n\n© KN-IT Team", disable_notification=True)
    sleep(7)
    bot.delete_message(message.chat.id, msg_start.message_id)
    bot.delete_message(message.chat.id, message.message_id)


# Handler for rules command
RULES = '''
ПРАВИЛА ЧАТА В КИЛЛНЕТ !!!

Никаких оскорблений, объявлений купли / продажи или предложений каких либо сервисов. Никаких реклам своих каналов и других источников.

Запрещенно оставлять ссылки на внешние источники, темболее с отработкой в JS, либо html.
Это в целях безопасности всех участников. В данном чате находятся люди далёкие от IT сферы.
Ссылки разрешенны на крупные и известные сайты, - если они конечно по теме.

За портянки и постоянные перепосты новостей - будет наложен мут, вплоть до исключения из группы.

Относитесь друг к другу с уважением! Если есть проблемы, пишите модераторам. Вы все люди, у вас есть правила приличия и этикет !

СОБЛЮДАЙТЕ ИХ !

Здесь Killnet детка - самая мощная и опасная группировка РФ.
❤🇷🇺❤

© KN-IT Team
'''
@bot.message_handler(commands=['rules', 'правила'])
def rules(message):

    msg_rules = bot.reply_to(message, RULES, disable_notification=True)
    sleep(40)
    bot.delete_message(message.chat.id, msg_rules.message_id)
    bot.delete_message(message.chat.id, message.message_id)

# Handler for help command
HELP = '''
Команды общего доступа

/help или /помощь - Эта команда вызывает меню помоши
/contact или /контакт - Эта команда покажет единственную официальную связь с KILLNET
/rules или /правила - Эта команда укажет на правила в чате

/mod или /мод -  Эта команда команда призовёт модераторов в чат

© KN-IT Team
'''
# /donate - Эта команда позволит увидеть как можно нас поддержать
@bot.message_handler(commands=['help', 'помощь'])
def help(message):

    msg_help = bot.reply_to(message, HELP, disable_notification=True)
    sleep(25)
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
@bot.message_handler(commands=['contact', 'контакт'])
def contact(message):

    msg_contact = bot.reply_to(message, CONTACT, disable_notification=True)
    sleep(45)
    bot.delete_message(message.chat.id, msg_contact.message_id)
    bot.delete_message(message.chat.id, message.message_id)

# Handler for DONATE command
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

# Temporary don't work
'''
@bot.message_handler(commands=['donate'])
def donate(message):

    msg_donate = bot.reply_to(message, DONATE, disable_notification=True)
    sleep(60)
    bot.delete_message(message.chat.id, msg_donate.message_id)
    bot.delete_message(message.chat.id, message.message_id)

'''

# Handler for mod command
MODERS = '''
Модераторы, обратите внимание на пост выше:
@Yary_kova @Snake_ebet_xoxlov @Ev1LcheF

© KN-IT Team
'''
@bot.message_handler(commands=['mod', 'мод'])
def moders(message):

    bot.reply_to(message, MODERS)


# Handler for getid command IsAdmin
@bot.message_handler(is_admin=True, commands=['getid', 'айди'])
def getid(message):
    if not message.reply_to_message:
        bot.reply_to(message, "🙄 Ошибка!\nНеобходимо ответить на сообщение. 😏\n\n© KN-IT Team")
        return
    
    # Admins cannot be deanoned
    user = bot.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status in ['administrator','creator']
    if user:
        bot.reply_to(message, "Ты чего это? 🤦‍♂\nНе пали админов... 😂\n\n© KN-IT Team")
        return
    


    name_gi = message.reply_to_message.from_user
    if name_gi.first_name == None:
        name_gi.first_name = "Не указанно"
    if name_gi.last_name == None:
        name_gi.last_name = "Не указанно"
    if name_gi.username == None:
        name_gi.username = "Отсутствует"
    if name_gi.language_code == None:
        name_gi.language_code = "Скрыто"
    if name_gi.is_premium == None:
        name_gi.is_premium = "Не премиум"
    if name_gi.is_premium == True:
        name_gi.is_premium = "Премиум"

    bot.reply_to(message, f"Вот что вижу через прицел:\n\nИмя: {name_gi.first_name}\nФамилия: {name_gi.last_name}\nЮзернейм: @{name_gi.username}\nUser_id: {name_gi.id}\nЯзык: {name_gi.language_code}\nТип: {name_gi.is_premium}\n\n© KN-IT Team", disable_notification=True)
    bot.delete_message(message.chat.id, message.message_id)  # remove admin message

# Handler for getid command NOTAdmin
@bot.message_handler(is_admin = False, commands=['getid', 'айди'])
def getusers(message):
    if not message.reply_to_message:
        bot.reply_to(message, "Вау!!\nТы знаешь волшебную команду...\nАккуратней с такой игрушкой, а то спалят тебя! 🤡\n\n© KN-IT Team")
        return

    bot.reply_to(message, "🤔 Чё нада?\nЩас в люлю дам... 🤧\n\n© KN-IT Team")


# Handler for TOO MANY WORDS - Is NOT Admin
@bot.message_handler(is_admin = False, func=lambda message: True)
def too_many_words(message):
    name = message.from_user
    if name.first_name == None:
        name.first_name = ""
    if name.last_name == None:
        name.last_name = ""
    msg_lens = len(message.text)
    #if msg_lens >= 800:
    #    bot.reply_to(message, f"Эй {name.first_name}, {name.last_name} Ебаааа... 😱\nДа тебе книги писать надо! Но здесь не место для этого, сорян 🤷‍♂\nСообщение удалено!\n\n© KN-IT Team")
    #    bot.delete_message(message.chat.id, message.message_id)
    if msg_lens >=850:
        bot.reply_to(message, "Что за портянка? 🤦‍♂\nПожалей участников чата!\nМодераторы - обратите внимание... 🙏\n\n© KN-IT Team")
    else:
        pass

# Handler for TOO MANY WORDS - Is Admin
@bot.message_handler(is_admin = True, func=lambda message: True)
def too_many_words(message):
    isadminname = message.from_user
    msg_lens= len(message.text)
    if msg_lens >= 600:
        bot.reply_to(message, f"Много букв всё-таки. Но ты же {isadminname.first_name}, а значит тебе всё можно 🤭\n\n© KN-IT Team")
    else:
        pass





# Do not forget to register filters
bot.add_custom_filter(IsAdmin())

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