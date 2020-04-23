import telebot
from telebot import apihelper,types
import requests
from time import sleep
from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest, ReadHistoryRequest
from telethon.sessions import StringSession
#from telethon.utils import InputPeerChannel

api_id = 995881               
api_hash = "e9d6b9e0826b56613da7a625b1ced401"              
phone_number = "+79521998467" 
bot = telebot.TeleBot('1102747678:AAEirVClMkXe3H_lAg43Ky-LiH2KekCTpiM')
session = '1ApWapzMBuyuAIbVp0jxeSyBGiRPWOXeqzfqBX7wuaFddqyqU2ioF68uSFK0cXCfO-y2Bt5wxtMxJqlGaihtL4Q763eMzdubxebwQyf7j9Sgvhjcz5zftvwIS-0RaVfhk5BY0EJ9HUx5fJifUBdgbhdr9xy76IQ6Roj9P-IdjYUSpa7lSHD_lMHfUdwca2C_dlRAXyfgmdys9IJMnXxZYPZsiAde2ICwgcGmzu27eUiRp41ym8GHv__OGtfnI60tsPOhpPqaG9EAwkZbVJwdoei2T84e0o7cDHIJa-ngiwCdXNTkCCoh0Lczb4kibOgJhzD6r82aPvqEYmMLJyHdoN0oo4f8_eIM'
client = TelegramClient('session_name', api_id, api_hash)
client.run_until_disconnected()
client.start()

balance = 0


@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Старт", callback_data="1")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Добрый день 111" + message.from_user.first_name + "! Приветсвуем Вас в боте поиска сообщений. Нажмите на кнопку «Старт» чтобы начать поиски.", reply_markup=keyboard)

@bot.message_handler(commands=["read"])
def read_chat(message):
    bot.send_message(message.from_user.id, "Введите название чата");
    bot.register_next_step_handler(message, get_chat);
    def get_chat(message):
        dp = client.get_entity(message)
        messages = client.get_messages(dp, limit=1)
        bot.send_message(message.chat.id, messages)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(message):

    if message.data == "1":
        bot.send_message(chat_id=message.message.chat.id, text = "Отлично...можете прислать ссылку на канал/чат, а после успешной проверки действительности ссылки с нашей стороны, отправьте слово, которое нужно поискать.")


# while True:
bot.polling(none_stop=True)
