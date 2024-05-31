from pyrogram import Client, filters
from pyrogram.errors import FloodWait

#from .. import loader, utils
import inspect
import asyncio

from pyrogram.types import ChatPermissions

import time
from time import sleep
import random

app = Client("my_account")
vkl=False
vklyu=False
tick = 0
ticki = 0
tickii = 0
timee = 0
func = 102
o100=False
o101=False
o102=False
name=0
args=1
zzz=2

# KomaHaa type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    global o100
    global o101
    global o102
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
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)


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
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)

#команда для бота
@app.on_message(filters.command("kop", prefixes=".") & filters.me)
def kop(_, msg):
    global vkl
    global tick
    global o100
    global o101
    global o102
    #vkl = False
    try:
        msg.edit("Модуль копания: start▶️")
        if vkl == True:
            msg.edit("Модуль копания: OFF❌")
            vkl = False
        elif vkl == False:
            msg.edit("Модуль копания: ON✅")
            vkl = True
        while vkl==True:
            msg.reply('Копать')
            tick += 1
            time.sleep(4)
            if tick==15:
                msg.reply('Продать Базальт III Все')
                tick=0
        
    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)

#для задержки
# @loader.tds
# class printer(loader.Module):
#     """Модуль для отправки сообщений боту"""
#     strings = {
#         "name": "Printer"
#     }
    
#     def __init__(self):
#         self.config = loader.ModuleConfig(
#             loader.ConfigValue(
#                 "chat_id", 5561185379,
#                 lambda: "Чат в который отправляются сообщения",
#                 validator=loader.validators.Integer()
#             ),
#             loader.ConfigValue(
#                 "cooldown", 2,
#                 lambda: "Задержка отправки",
#                 validator=loader.validators.Float()
#             )
#         )
    
#     async def client_ready(self):
#         if self.get("status") == None: self.set("status", False)
#         if self.get("status"): await self.send()
        
    
#     @loader.command()
#     async def zzz(self, message):
#         ''' - Изменить задержку отправки ( В секундах )'''
#         args = utils.get_args_raw(message)
#         cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name}'
#         if args:
#             cmd = f'{utils.escape_html(self.get_prefix())}{inspect.currentframe().f_code.co_name} {utils.get_args_raw(message)}'
#         try:
#             args = float(args)
#             self.config["cooldown"] = args
#             await utils.answer(message, f"<emoji document_id=5332533929020761310>✅</emoji><b>Успешно!\nЗадержка изменена на {args}</b> ")
#         except ValueError:
#             await utils.answer(message, f"<emoji document_id=5240241223632954241>⛔</emoji><b> Ошибка | Нужно указать число</b>")

#extra
@app.on_message(filters.command("kon", prefixes=".") & filters.me)
def kon(_, msg):
    global vklyu
    global ticki
    global tickii
    global timee
    global func
    global o100
    global o101
    global o102
    global args
    global zzz
    #vkl = False
    try:
        msg.edit("Модуль отправки: start▶️")
        if func==102:
            msg.reply("⛔❗Ошибка: 102 | Проверьте код")
            o102=True
            func=0
        if func!=102:
            if vklyu == True:
                msg.edit("Модуль отправки: OFF❌")
                vklyu = False
                func=0
            elif vklyu == False:
                msg.edit("Модуль отправки: ON✅")
                vklyu = True
                func=0
            while vklyu==True and ticki!=5 and ticki<5:
                msg.reply('/cum')
                ticki += 1
                tickii += 1
                time.sleep(zzz)
                if ticki>=5:
                    msg.reply('Юз кириешки')
                    ticki=0
                if tickii>=1300:
                    msg.reply(f"Отладка: tick = {tickii}. Перезагрузка🔄.")
                    vklyu=False
                    vklyu=True
                    tickii=0
                elif tickii>=1400:
                    msg.reply('⛔❗Ошибка: 101')
                    o101=True
                if timee>=2700:
                    kon
                    vklyu=False
                    vklyu=True
                    msg.reply(f'Переменная = {vklyu}. Перезагрузка 2🔄.')
                    timee = 0
                elif timee>=2800:
                    msg.reply('⛔❗Ошибка: 101. Time обнулена')
                    o101=True
                    timee = 0
            while vklyu==True:
                timee+=1
                time.sleep(1)
            
        
    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)    

#задержка
@app.on_message(filters.command("zzz825", prefixes=".") & filters.me)
def zzz825(_, msg):
    global vklyu
    global ticki
    global tickii
    global timee
    global func
    global o100
    global o101
    global o102
    global zzz
    try:
        msg.edit('Задержка была изменена на 0.825')
        zzz=0.825

    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)  

@app.on_message(filters.command("zzz09", prefixes=".") & filters.me)
def zzz09(_, msg):
    global vklyu
    global ticki
    global tickii
    global timee
    global func
    global o100
    global o101
    global o102
    global zzz
    try:
        msg.edit('Задержка была изменена на 0.9')
        zzz=0.9

    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)  

@app.on_message(filters.command("zzz12", prefixes=".") & filters.me)
def zzz12(_, msg):
    global vklyu
    global ticki
    global tickii
    global timee
    global func
    global o100
    global o101
    global o102
    global zzz
    try:
        msg.edit('Задержка была изменена на 1.2')
        zzz=1.2

    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)  

@app.on_message(filters.command("zzz17", prefixes=".") & filters.me)
def zzz17(_, msg):
    global vklyu
    global ticki
    global tickii
    global timee
    global func
    global o100
    global o101
    global o102
    global zzz
    try:
        msg.edit('Задержка была изменена на 1.7')
        zzz=1.7

    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)  




#модуль отладки
@app.on_message(filters.command("otl", prefixes=".") & filters.me)
def otl(_, msg):
    global vklyu
    global ticki
    global tickii
    global o100
    global o101
    global o102
    try:
        msg.edit('📶❗')
        time.sleep(1.5)
        msg.edit(f"🅿️ℹ️🆖Отладка: tick = {tickii}")
        if o100==True:
            msg.reply('Список ошибок: **Ошибка 100** — __ошибка из-за спама__')
        elif o101==True:
            msg.reply('Список ошибок: **Ошибка 101** — __ошибка из-за переполнения переменных__')
        elif o102==True:
            msg.reply('Список ошибок: **Ошибка 102** — __ошибка из-за сбоя основной функции__')
    except FloodWait as e:
            msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
            o100=True
            sleep(5)
#отладка админ
# @app.on_message(filters.command(f"otla{name==input()}", prefixes=".") & filters.me)
# def otla(_, msg):
#     global vklyu
#     global name
#     global ticki
#     global tickii
#     global timee
#     global func
#     global o100
#     global o101
#     global o102
#     try:
#         if name=='lol': 
#             msg.reply('lol')
#     except FloodWait as e:
#             msg.reply("⛔❗Ошибка: 100                                                                        Подождите 5 секунд")
#             o100=True
#             sleep(5)

# Команда взлома пентагона
@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
    global o100
    global o101
    global o102
 
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
            msg.reply("⛔❗Ошибка: 100                                                              Подождите 5 секунд")
            o100=True
            sleep(5)
 
    msg.edit("🦖 Найдены данные о существовании динозавров на земле!")

app.run()


#