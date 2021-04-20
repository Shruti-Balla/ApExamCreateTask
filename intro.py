import turtle
import sys
from time import sleep
from easyTypeWriter import typeWriter
import winsound

wn = turtle.Screen()
wn.setup(600,600)
wn.bgpic("sky.gif")
# message = "Hello"

#obj = typeWriter.EasyInput()
words = "Hello! Welcome to our typing game! :P"
'''
obj.setEnterAudioPath("C:/Users/astro/Downloads/word_game_AP.py/ding3.wav")
obj.setKeyboardAudioPath("C:/Users/astro/Downloads/word_game_AP.py/keyhee.wav")
x = obj.takeInput(True , words)
'''
for char in words:
    sleep(0)
    sys.stdout.write(char)
    sys.stdout.flush()
    winsound.PlaySound('keyhee.wav', winsound.SND_FILENAME)
