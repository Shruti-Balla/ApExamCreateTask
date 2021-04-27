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
def clearScreen():
  os.system("clear")

for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
    winsound.PlaySound('keyhee.wav', winsound.SND_FILENAME)
    
words = "Instructions: type as many words as accurately as you can before the timer runs out. Good luck and have fun!"
def clearScreen():
  os.system("clear")

for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()
    winsound.PlaySound('keyhee.wav', winsound.SND_FILENAME)
    
sleep(1)
clearScreen()

wn.mainloop()
