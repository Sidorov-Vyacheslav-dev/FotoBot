import yadisk
import aiofiles
import random
from config_data.config import Config, load_config

config: Config = load_config()


client=yadisk.Client(token=config.tg_bot.aouth_token)

def image(path):
    with client:
        #print(client.check_token())
        #URL = client.get_download_link(random.choice(my_image))
        URL = random.choice(list(client.listdir(path)))['file']
    #await bot.send_photo(chat_id=message.chat.id, photo=URL
    return URL

def folder():
    folders=[]
    with client:
        #URL = client.get_download_link(random.choice(my_image))
        text1 = list(client.listdir("/bot"))
    for i in text1:
        folders.append(i['name'])
    return folders
