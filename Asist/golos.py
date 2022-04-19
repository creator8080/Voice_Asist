import speech_recognition as sr
import pyttsx3
import time
from fuzzywuzzy import fuzz
import datetime
from tkinter import * 
import golos2
import subprocess
import os
from translate import Translator
import webbrowser
import re
import pyglet
import random
import requests
from bs4 import BeautifulSoup
import wikipedia

spek=pyttsx3.init()
def speak(text):
    print(text)
    spek.say(text)
    spek.runAndWait()

opts = {
    "TimeTimes": ('минута','минуты','минуту','минут'),
    "TimeSeconds":('секунд','секунду','секунды','секунда'),
    "alias": ('candy','кеша','геннадий','гена'),
    "cmds": {
        "ctime": ('время','час','время','время','времени'),
        "kalkulater": ('+','-','/','х'),
        "perevod": ('переведи','перевод'),
        "Poisk":('google', 'поиск', 'найти','найди'),
        "Timer":('засеки таймер','таймер'),
        "game": ('змейка игра игру запусти'),
        "dol": ('курс', 'доллара', 'долара', 'доллар', 'долар', '$'),
        "monetka": ('подкинь' 'монетку' 'подкинуть','кинь')
    }
}

def rec():
    global kal
    r=sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        audio = r.listen(source)
    try:
        voice = r.recognize_google(audio, language = "ru-RU").lower()
        print("[log] "+ voice)
        with open('filik.txt','w') as f:
            f.write(voice)

        cmd = voice
        for x in opts['alias']:
            cmd=kal= cmd.replace(x, "").strip()

        cmd = recognize_cmd(cmd)
        funck(cmd['cmd']) 

    except sr.UnknownValueError:
        rec
    except sr.RequestError as e:
        speak("[log] Неизвестная ошибка, проверьте интернет или код!")
def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    
    return RC
def funck(cmd):
    if cmd == "Poisk":
        wikipedia.set_lang("ru") 
        speak('Что узнать')
        with open('filik2.txt','w') as f:
            f.write('Что узнать?')
        r=sr.Recognizer()
        with sr.Microphone(device_index = 1) as source:
            audio = r.listen(source)
        what = r.recognize_google(audio, language = "ru-RU").lower()
        with open('filik.txt','w') as f:
            f.write(what)
        speak(wikipedia.summary(what, sentences=5))

    elif cmd == 'ctime':
        now = datetime.datetime.now()
        with open('filik2.txt','w') as f:
            f.write("Сейчас " + str(now.hour) + ":" + str(now.minute))
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
    elif cmd == 'kalkulater':
        print(kal)
        kaling = kal.replace('и','') 
        kaling1 = kaling.replace('х','*')
        summa = eval(kaling1)
        with open('filik2.txt','w') as f:
            f.write(summa)
        speak(summa)
    elif cmd == "perevod":
        r=sr.Recognizer()
        with open('filik2.txt','w') as f:
            f.write('Что перевести?')
        speak("что перевести?")
        with sr.Microphone(device_index = 1) as source:
            audio = r.listen(source)
        perevodim = r.recognize_google(audio, language = "ru-RU").lower()
        with open('filik.txt','w') as f:
            f.write(perevodim)
        translator= Translator(from_lang="russian",to_lang="English")
        translation = translator.translate(perevodim)
        with open('filik2.txt','w') as f:
            f.write(translation)
        speak(translation)
    elif cmd == "Timer":
        with open('filik2.txt','w') as f:
            f.write("На какое время поставить таймер?")
        speak("на какое время поставить таймер")
        r=sr.Recognizer()
        with sr.Microphone(device_index = 1) as source:
            audio = r.listen(source)
        times = r.recognize_google(audio, language = "ru-RU").lower()
        with open('filik.txt','w') as f:
            f.write(times)
        for x in opts['TimeTimes']:
            min = times.split(x)[0]
        for y in opts['TimeTimes']:
            sec = times.split(y)[-1]
            for z in opts['TimeSeconds']:
                sec = sec.split(z)[0]
                sec = re.sub('\D', '', sec)
        min= int(min) * 60
        timerING = int(min) + int(sec)
        with open('filik2.txt','w') as f:
            f.write("Вы поставили таймер на: "+ str(timerING) + " секунды!")
        speak("вы поставили таймер на: "+ str(timerING) + " секунды")
        time.sleep(int(timerING))
        with open('filik2.txt','w') as f:
            f.write("Таймер завершён")
        speak("Таймер завершён")
    elif cmd == "monetka":
        mon = random.randint(1, 2)
        if mon == 1:
            with open('filik.txt','w') as f:
                f.write("Орёл")
            speak("Орёл")
        else:
            with open('filik.txt','w') as f:
                f.write("Решка")
            speak("Решка")
    elif cmd == "dol":
        with open('filik.txt','w') as f:
                f.write("Открываю...")
        subprocess.Popen('python Dolar.py')
    elif cmd == "game":
        with open('filik.txt','w') as f:
                f.write("Запуск...")
        subprocess.Popen('python game.py')
    else:
        print('https://yandex.ru/search/?text=' + cmd)
    subprocess.Popen('python golos2.py')
   

    




