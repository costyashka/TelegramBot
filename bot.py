import asyncio
import concurrent.futures
import logging
import sqlite3
import time

import telebot
from telebot import apihelper

from telethon import TelegramClient, sync, events, connection

#logging.basicConfig(level=logging.DEBUG)
CHECKER = True
TOKEN = '1102747678:AAEirVClMkXe3H_lAg43Ky-LiH2KekCTpiM'
conn = sqlite3.connect('users.db',check_same_thread=False)
cursor = conn.cursor()
bot = telebot.AsyncTeleBot(TOKEN,num_threads=3)

apihelper.proxy = {'http': '151.253.165.70:8080','https': '151.253.165.70:8080'}


def check_new():
    print('Start cheking')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    bot = telebot.AsyncTeleBot(TOKEN,num_threads=3)
    proxy = ('proxy.digitalresistance.dog',443,'d41d8cd98f00b204e9800998ecf8427e')
    api_hash = "e9d6b9e0826b56613da7a625b1ced401" 
    api_id = 995881
    client = TelegramClient('session_name', api_id, api_hash, proxy=proxy,  
            connection=connection.tcpmtproxy.ConnectionTcpMTProxyRandomizedIntermediate)

    client.connect()
    while CHECKER:
        print('Checking...')
        cursor.execute("select * from users")
        for i in cursor.fetchall():
            temp = 0
            print('Work with',i)
            dp = client.get_entity(i[1])
            messages = client.get_messages(dp,limit=100,min_id=1)
            for j in messages:
                temp = max(j.id,temp)
                if i[3] in j.text:
                    bot.send_message(i[1],j.text)
            print('???',j.id,i[0],i[1])
            cursor.execute("update users set Last_id = {} where User_id = '{}' and Channel_id = '{}'".format(temp,i[0],i[1]))
            conn.commit()
            print('!!!')
            time.sleep(1)
        time.sleep(15)
        print('END CHECK')
    bot.polling()

    conn.close()
    client.disconnect()

def func(url):
    print('Start parsing')
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    proxy = ('proxy.digitalresistance.dog',443,'d41d8cd98f00b204e9800998ecf8427e')
    api_hash = "e9d6b9e0826b56613da7a625b1ced401" 
    api_id = 995881
    client = TelegramClient('session_name', api_id, api_hash, proxy=proxy,  
            connection=connection.tcpmtproxy.ConnectionTcpMTProxyRandomizedIntermediate)
    print('qwer')
    client.connect()
    dp = client.get_entity(url)
    messages = client.get_messages(dp,limit=100)
    client.disconnect()
    return messages


def botf():
    @bot.message_handler(commands=['start'])
    def get_start(message):
        #bot.send_message(message.from_user.id,"Для чтения телеграмм канала введите следующее: /read [Ссылка на канал] [Количество сообщений (число)]")
        bot.send_message(message.from_user.id,"Для чтения телеграмм канала введите следующее: /read [Ссылка на канал] [фильтр]")
    
    @bot.message_handler(commands=['read'])
    def get_text_messages(message):
        comm = list(message.text.split())
        print(comm[2])
        if len(comm) == 3:
            try:
                print(1)
                x = concurrent.futures.ThreadPoolExecutor().submit(func,comm[1])
                print(x.done)
                messages = x.result()
                print(3)
                print(len(messages))
                #bot.send_message(message.from_user.id,i.text)
                for i in messages:
                    if comm[2] in i.text:
                        #print(i.to_id)
                        bot.send_message(message.from_user.id,i.text)
                        #bot.send_message("@clickname","tet")
                print(4)
            except ZeroDivisionError:
                bot.send_message(message.from_user.id,"Вы ввели неверный адресс")

    @bot.message_handler(commands=['reg'])
    def reg_users(message):
        comm = list(message.text.split())
        cursor.execute("insert into users values ('{}','{}',{},'{}')".format(message.from_user.id,comm[1],0,comm[2]))
        print('ok')
        conn.commit()
    bot.polling()

y = concurrent.futures.ThreadPoolExecutor().submit(check_new)
botf()
