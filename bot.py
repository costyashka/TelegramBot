import telebot
from telebot import apihelper,types
import requests
from time import sleep

bot = telebot.TeleBot('1102747678:AAEirVClMkXe3H_lAg43Ky-LiH2KekCTpiM')
#apihelper.proxy = {'https':'socks5://85.10.235.14:1080'}
apihelper.proxy = {
    'https5': '138.197.157.32:1080'
}

balance = 0


@bot.message_handler(commands=['start'])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Старт", callback_data="1")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "Добрый день 111" + message.from_user.first_name + "! Приветсвуем Вас в боте поиска сообщений. Нажмите на кнопку «Старт» чтобы начать поиски.", reply_markup=keyboard)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(message):

#     if message.data == "1":
#         bot.send_message(chat_id=message.message.chat.id, text = "Отлично...можете прислать ссылку на канал/чат, а после успешной проверки действительности ссылки с нашей стороны, отправьте слово, которое нужно поискать.")


# while True:
bot.polling(none_stop=True, interval=0)
