from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")
vkl=False
vklyu=False
tick = 0
ticki = 0
# KomaHaa type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "▒"
        # вот так
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol) #печать части сообщения + символ каретки  # -"▒" -1 проход на 2-ом и следующих:  "в▒" 
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]  # сообщение увеличеть на первый символ входящего сообщения
            text = text[1:]     # входящее сообщение  -  удалить первый символ
 
            msg.edit(tbp)    # печать без каретки(typing_symbol)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)


@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(_, msg):
   
    try:
        text=msg.text.split(".help ", maxsplit=1)

        coun=1
        orig_text="*"
        orig_text2="#" #text.text.split(" ", maxsplit=1)
        coun=len(text)
        if coun>1:
            orig_text = text[1]
            orig_text2=orig_text.text.split(" ", maxsplit=1)


        for e in [orig_text2]:
           msg.reply(e)  


        #orig_text = msg.text.split(".help ", maxsplit=1)[1]
        
        #orig_text2 = msg.text.split(".help ", maxsplit=1)[2]
        msg.edit("HELP")
        msg.reply("type")
        msg.reply(orig_text)
        msg.reply(orig_text2)
       
    except FloodWait as e:
            sleep(e.x)   
            msg.reply("error")      

#команда для бота
@app.on_message(filters.command("kop", prefixes=".") & filters.me)
def kop(_, msg):
    global vkl
    global tick
    #vkl = False
    try:
        msg.edit("kop: start")
        if vkl == True:
            msg.edit("kop: OFF")
            vkl = False
        elif vkl == False:
            msg.edit("kop: ON")
            vkl = True
        while vkl==True:
            msg.reply('Копать')
            tick += 1
            time.sleep(4)
            if tick==15:
                msg.reply('Продать Базальт III Все')
                tick=0
        
    except FloodWait as e:
            sleep(e.x)     
#extra
@app.on_message(filters.command("kon", prefixes=".") & filters.me)
def kon(_, msg):
    global vklyu
    global ticki
    #vkl = False
    try:
        msg.edit("kon: start")
        if vklyu == True:
            msg.edit("kon: OFF")
            vklyu = False
        elif vklyu == False:
            msg.edit("kon: ON")
            vklyu = True
        while vklyu==True:
            msg.reply('Кончить')
            ticki += 1
            time.sleep(1.2)
            if ticki==3:
                msg.reply('Юз кириешки')
                ticki=0
        
    except FloodWait as e:
            sleep(e.x)     


# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮‍ Взлом пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(2)
 
    msg.edit("👽 Поиск секретных данных об НЛО ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "👽 Поиск секретных данных об НЛО ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

app.run()


#