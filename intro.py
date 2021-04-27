import turtle
import sys
from time import sleep
from easyTypeWriter import typeWriter
import winsound
#sound credit goes to harshnative on github

wn = turtle.Screen()
wn.setup(600,600)
sky =('sky.gif')
wn.bgpic(sky)
# message = "Hello"

obj = typeWriter.EasyInput()
words = "Hello! Welcome to our typing game! :P"

for char in words:
    sleep(0)
    sys.stdout.write(char)
    sys.stdout.flush()
    winsound.PlaySound('keyhee.wav', winsound.SND_FILENAME)

wn.mainloop()
