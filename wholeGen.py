import pyautogui
from time import sleep
import sys
import json
from ast import literal_eval
notes ={
    "C3":"q",
    "D3":"w",
    "E3":"e",
    "F3":"r",
    "G3":"t",
    "A3":"y",
    "B3":"u",

    "C2":"a",
    "D2":"s",
    "E2":"d",
    "F2":"f",
    "G2":"g",
    "A2":"h",
    "B2":"j",

    "C1":"z",
    "D1":"x",
    "E1":"c",
    "F1":"v",
    "G1":"b",
    "A1":"n",
    "B1":"m",
}

lens={
    "2":1,
    "1":0.5,
    "0.5":0.25
}

# minim 1 crotchet 0.5 quaver 0.25
print("starting auto in 5 seconds:")
sleep(5)

pyautogui.PAUSE = 0
#song2 = open("zelda_Lullaby.txt")
hk=[]
song2 = open(sys.argv[1])
song = literal_eval(song2.read())
last = 0
for n in song:
    #pyautogui.press(notes[n])
    for x in n[1]:
        pyautogui.press(notes[x])
    if float(n[0]) > 0:  
        sleep(float(n[0])*0.666)

