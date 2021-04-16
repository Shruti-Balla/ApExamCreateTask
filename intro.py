import turtle
import sys
from time import sleep

words = "Hello! Welcome to our typing game! :P"
for char in words:
    sleep(0.2)
    sys.stdout.write(char)
    sys.stdout.flush()
