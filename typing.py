import turtle
import os
import sys
from time import sleep

wn = turtle.Screen()
wn.setup(600,600)
wn.bgpic("sky.gif")
# message = "Hello"

turtle = turtle.Turtle()
turtle.hideturtle()

index = 0
words = "Hello! Welcome to our typing game!"

turtle.penup()
turtle.goto(-200, 0)

for char in words:
    index += 1
    sleep(0.1)
    turtle.pendown()
    turtle.write(char, align="center", font=("Times New Roman", 35, "normal"))
    turtle.penup()
    turtle.goto(turtle.xcor() + 24, turtle.ycor())
    if index == 14:
      turtle.goto(-275,-50)
    sys.stdout.flush()

sleep(1)
turtle.clear()

index = 0
words = "Instructions: type as many words as accurately as you can before the timer runs out. Good luck and have fun!"

turtle.penup()
turtle.goto(-200, 0)

for char in words:
    index += 1
    sleep(0.1)
    turtle.pendown()
    turtle.write(char, align="center", font=("Times New Roman", 35, "normal"))
    turtle.penup()
    turtle.goto(turtle.xcor() + 24, turtle.ycor())
    if index == 14:
      turtle.goto(-275,-50)
    sys.stdout.flush()

sleep(1)
turtle.clear()
