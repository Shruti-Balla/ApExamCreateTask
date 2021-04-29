import turtle
import os
import sys
from time import sleep

wn = turtle.Screen()
wn.setup(600,600)
wn.bgpic("sky.gif")

turtle = turtle.Turtle()
turtle.hideturtle()

index = 0
words = "Hello! Welcome to our typing game!"

turtle.penup()
turtle.goto(-150, 30)

for char in words:
    index += 1
    sleep(0.02)
    turtle.pendown()
    turtle.write(char, align="center", font=("Times New Roman", 25, "normal"))
    turtle.penup()
    turtle.goto(turtle.xcor() + 20, turtle.ycor())
    if index == 14:
      turtle.goto(-225, -20)
    sys.stdout.flush()

sleep(1)
turtle.clear()

index = 0
words = "Instructions: type as many words as accurately as you can before the timer runs out. Good luck and have fun!"

turtle.penup()
turtle.goto(-200, 90)

for char in words:
    index += 1
    sleep(0.02)
    turtle.pendown()
    turtle.write(char, align="center", font=("Times New Roman", 25, "normal"))
    turtle.penup()
    turtle.goto(turtle.xcor() + 20, turtle.ycor())
    if index == 19:
      turtle.goto(-275, 40)
    if index == 47:
      turtle.goto(-275, -10)
    if index == 75:
      turtle.goto(-275, -60)
    if index == 103:
      turtle.goto(-60, -110)
    sys.stdout.flush()

sleep(1)
turtle.clear()
