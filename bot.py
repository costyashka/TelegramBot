import telebot
from telebot import apihelper,types
import requests
from time import sleep
from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest, ReadHistoryRequest
from telethon.utils import InputPeerChannel

api_id = 995881               # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = "e9d6b9e0826b56613da7a625b1ced401"              # API Hash (оттуда же)
phone_number = "+79521998467" 
bot = telebot.TeleBot('1102747678:AAEirVClMkXe3H_lAg43Ky-LiH2KekCTpiM')
client = TelegramClient('session_name', api_id, api_hash)
client.start()

balance = 0


@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Старт", callback_data="1")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Добрый день 111" + message.from_user.first_name + "! Приветсвуем Вас в боте поиска сообщений. Нажмите на кнопку «Старт» чтобы начать поиски.", reply_markup=keyboard)

@bot.message_handler(commands=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, "message.text")
    messages = client.get_entity('Telegram')
    bot.send_message(message.chat.id, messages)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(message):

    if message.data == "1":
        bot.send_message(chat_id=message.message.chat.id, text = "Отлично...можете прислать ссылку на канал/чат, а после успешной проверки действительности ссылки с нашей стороны, отправьте слово, которое нужно поискать.")


# while True:
bot.polling(none_stop=True)
