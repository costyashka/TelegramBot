import telebot

bot = telebot.TeleBot('1102747678:AAEirVClMkXe3H_lAg43Ky-LiH2KekCTpiM')

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)