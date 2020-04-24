import telebot
from telebot import apihelper
import logging
from bot import func
logging.basicConfig(level=logging.DEBUG)

bot = telebot.TeleBot('1102747678:AAEirVClMkXe3H_lAg43Ky-LiH2KekCTpiM')
apihelper.proxy = {'https':'http://81.210.32.101:8080'}

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)
    print(func(url='@teleblog',num=2))

if __name__ == '__main__':
     bot.polling(none_stop=True)