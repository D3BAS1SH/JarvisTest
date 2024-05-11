import subprocess
import ApplicationLocal as AL
import os
import pyautogui as PAG
import random
import requests as REQ

def OpenApps(x):
    if(x.lower()=='notepad'):
        subprocess.Popen(AL.path['notepad'])
    elif x.lower()=='discord':
        subprocess.Popen(AL.path['discord'])
    elif x.lower()=='calculator':
        subprocess.Popen(AL.path['calculator'])
    elif x.lower()=='code':
        subprocess.Popen(AL.path['code'])
    elif x.lower()=='steam':
        subprocess.Popen(AL.path['steam'])
    elif x.lower()=='camera':
        os.system('start microsoft.windows.camera:')
    else:
        return "Can not find such application."

def OpenDir(x):
    if(x.lower()=='this pc' or x.lower()=='computer' or x.lower()=='my computer'):
        PAG.hotkey('win','e')
    elif x.lower()=='c drive':
        os.startfile('C:')
    elif x.lower()=='d drive':
        os.startfile('D:')
    else:
        return "No such drive found."

""" def getInfos(x):
    if x.lower()=='ip':
         """

def Greet(name):
    return f"Morning {name}"

def getRandomReplyRes():
    return AL.ActionResponseSpeech[random.randint(0,len(AL.ActionResponseSpeech)-1)]

def getIP():
    return REQ.get('https://api64.ipify.org/?format=json').json()['ip']

print(getIP())