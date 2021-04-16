import os
import sys
from time import sleep

words = "Hello! Welcome to our typing game!"
def clearScreen():
  os.system("clear")

for char in words:
    sleep(0.1)
    sys.stdout.write(char)
    sys.stdout.flush()

sleep(1)
clearScreen()
