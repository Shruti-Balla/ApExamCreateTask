import turtle
from PIL import ImageTk, Image
import sys
from time import sleep
from easyTypeWriter import typeWriter
import winsound

wn = turtle.Screen()
wn.setup(600,600)
sky =('sky.gif')
wn.bgpic(sky)
# message = "Hello"

#obj = typeWriter.EasyInput()
#swords = "Hello! Welcome to our typing game! :P"
'''
obj.setEnterAudioPath("C:/Users/astro/Downloads/word_game_AP.py/ding3.wav")
obj.setKeyboardAudioPath("C:/Users/astro/Downloads/word_game_AP.py/keyhee.wav")
x = obj.takeInput(True , words)
'''
'''for char in words:
    sleep(0)
    sys.stdout.write(char)
    sys.stdout.flush()
    winsound.PlaySound('keyhee.wav', winsound.SND_FILENAME)'''

wn.mainloop()
