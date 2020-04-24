
from telethon import TelegramClient, sync, events, connection
from telethon.tl.functions.channels import GetMessagesRequest
from telethon.tl.functions.messages import GetHistoryRequest, ReadHistoryRequest
import logging
#logging.basicConfig(level=logging.DEBUG)
#from telethon.utils import InputPeerChannel
url = input('Input link to Telegram channel: ')
num = int(input('Input a number of posts: '))

def func(url = url,num=num):
    proxy = ('proxy.digitalresistance.dog',443,'d41d8cd98f00b204e9800998ecf8427e')
    api_hash = "e9d6b9e0826b56613da7a625b1ced401" 
    api_id = 995881
    client = TelegramClient('session_name', api_id, api_hash, proxy=proxy,  
        connection=connection.tcpmtproxy.ConnectionTcpMTProxyRandomizedIntermediate)

    client.connect()
    dp = client.get_entity(url)
    messages = client.get_messages(dp,limit=num)
    for i in messages: #все сообщения в массиве messages, если консольный вывод не нужен, то сотрите этот цикл
        try:
            print(i.to_dict()['message'])
            print('----------')
        except Exception:
            pass
    return len(messages)
func()
