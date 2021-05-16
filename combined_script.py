#-----TYPING GAME-----

# import modules turtle, time, random, RandomWords
import turtle
from time import sleep
import random
import os
import sys
from random_words import RandomWords
import winsound
#sound credit goes to headspace

s = turtle.Screen()
s.setup(600,600)
s.bgpic('sky.gif')

s.addshape('cloud.gif')

# initialize variables
rw = RandomWords()
words = rw.random_words(count=1000)
turtles = []
string = ""
strings = words
random.shuffle(strings)
characters = []
index = 0
initial_x = random.randint(-300, 10)
initial_y = random.randint(-300, 10)
letter = ""
words_typed = 0
cleared = True
gameover = False
message = turtle.Turtle()
message.hideturtle()
cloud = turtle.Turtle()
cloud.hideturtle()
last_string = ""




# begin game - make the first letter blue
def begin_game():
    global index
    global letter
    global cleared
    global strings
    global last_string
    
    index = 0
    turtles[0].clear()
    turtles[0].color("blue")
    turtles[0].write(characters[0], align="center", font=("Arial", 30, "normal", "underline"))
    letter = characters[0]
    cleared = False
    if gameover == True:
        s.clear()
        s.bgpic('sky.gif')
        last_string = strings[i-1]

# puts writers and characters at corresponding indexes
def initialize(new_string):
    global string
    global initial_x
    global initial_y
    global index
    global cleared
    global last_string

    index = 0
    print(new_string)
    for character in new_string:
        string = new_string
        writer = turtle.Turtle()
        turtles.append(writer)
        characters.append(character)
        writer.speed(8)
        writer.penup()
        writer.hideturtle()

    # writes a character at the corresponding index of the writer
    for writer in turtles:
        if gameover == True:
            last_string = strings[i-1]
            writer.clear()
            break
        else:
            print(new_string[index]) 
            writer.goto(initial_x, initial_y) # change location
            writer.write(characters[index], align="center", font=("Arial", 30, "normal"))
            index += 1
            initial_x += 25
            if gameover == True:
                last_string = strings[i-1]
                writer.clear()
                break
    initial_x = random.randint(-300, 10)
    initial_y = random.randint(-300, 10)
    begin_game() # writes word
    
# move on to the next word in the list
i = 0
def next_word(x=2,y=3):
    global i
    global message
    global cloud
    global cleared

    while cleared:
        if gameover == True:
            for writer in turtles:
                writer.clear()
            s.clear()
            s.bgpic('sky.gif')
        if strings[i-1] == last_string:
            i += 1
        message.clear()
        cloud.hideturtle()
        cloud.shape("circle")
        initialize(strings[i])
        i += 1   

# game over screen
def game_over():
    global i
    global gameover
    global cleared
    global message
    global cloud
    global index
    global seconds
    global main

    # writes game over
    s.clear()
    s.bgpic('sky.gif')
    message.goto(0, 0)
    message.write("GAME OVER!", align="center", font=("Times New Roman", 70, "normal"))

    # displays total words typed
    message.goto(0, -50)
    message.write("You typed a grand total of " + str(words_typed) + " word(s)!", align="center", font=("Times New Roman", 20, "normal"))

    # play again button
    cloud.shape("cloud.gif")
    cloud.penup()
    cloud.goto(0, -150)
    cloud.showturtle()
    gameover = False
    cleared = True
    i += 1
    turtles.clear() # clears the writers
    characters.clear() # clears the character list
    main.write("Time: ", font=("Times New Roman", 30, "normal"))
    seconds = 15
    cloud.onclick(next_word)
    s.onkeypress(trigger_update_a, "a")
    s.onkeypress(trigger_update_b, "b")
    s.onkeypress(trigger_update_c, "c")
    s.onkeypress(trigger_update_d, "d")
    s.onkeypress(trigger_update_e, "e")
    s.onkeypress(trigger_update_f, "f")
    s.onkeypress(trigger_update_g, "g")
    s.onkeypress(trigger_update_h, "h")
    s.onkeypress(trigger_update_i, "i")
    s.onkeypress(trigger_update_j, "j")
    s.onkeypress(trigger_update_k, "k")
    s.onkeypress(trigger_update_l, "l")
    s.onkeypress(trigger_update_m, "m")
    s.onkeypress(trigger_update_n, "n")
    s.onkeypress(trigger_update_o, "o")
    s.onkeypress(trigger_update_p, "p")
    s.onkeypress(trigger_update_q, "q")
    s.onkeypress(trigger_update_r, "r")
    s.onkeypress(trigger_update_s, "s")
    s.onkeypress(trigger_update_t, "t")
    s.onkeypress(trigger_update_u, "u")
    s.onkeypress(trigger_update_v, "v")
    s.onkeypress(trigger_update_w, "w")
    s.onkeypress(trigger_update_x, "x")
    s.onkeypress(trigger_update_y, "y")
    s.onkeypress(trigger_update_z, "z")

    s.ontimer(update_countdown, t=1000)


# display countdown
timer_turtle = turtle.Turtle()
main = turtle.Turtle()
main.hideturtle()
main.penup()
main.goto(125, 200)
main.pendown()
main.write("Time: ", font=("Times New Roman", 30, "normal"))
timer_turtle.hideturtle()
timer_turtle.color("Red")
timer_turtle.penup()
timer_turtle.goto(225, 200)
timer_turtle.pendown()
seconds = 15

def update_countdown():
    global seconds
    global gameover
    global last_string

    timer_turtle.clear()
    timer_turtle.write(str(seconds), font=("Times New Roman", 30, "normal"))
    seconds -= 1
    if seconds == -1:
        gameover = True
        game_over()
        #winsound.PlaySound('Ping2.wav', winsound.SND_FILENAME)
        last_string = strings[i]
    else:
        s.ontimer(update_countdown, t=1000)


# create a timer

intro_turtle = turtle.Turtle()
intro_turtle.hideturtle()
word_index = 0
intro = "Hello! Welcome to our typing game!"
intro_turtle.penup()
intro_turtle.goto(-150, 30)

# first intro message
for char in intro:
    word_index += 1
    sleep(0.02)
    intro_turtle.pendown()
    intro_turtle.write(char, align="center", font=("Times New Roman", 25, "normal"))
    intro_turtle.penup()
    intro_turtle.goto(intro_turtle.xcor() + 20, intro_turtle.ycor())
    if word_index == 14:
      intro_turtle.goto(-225, -20)
    sys.stdout.flush()
sleep(1)
intro_turtle.clear()
word_index = 0
intro = "Instructions: type as many words as accurately as you can before the timer runs out. Good luck and have fun!"
intro_turtle.penup()
intro_turtle.goto(-200, 90)

# second intro message
for char in intro:
    word_index += 1
    sleep(0.02)
    intro_turtle.pendown()
    intro_turtle.write(char, align="center", font=("Times New Roman", 25, "normal"))
    intro_turtle.penup()
    intro_turtle.goto(intro_turtle.xcor() + 20, intro_turtle.ycor())
    if word_index == 19:
      intro_turtle.goto(-275,40)
    if word_index == 47:
      intro_turtle.goto(-275,-10)
    if word_index == 75:
      intro_turtle.goto(-275,-60)
    if word_index == 103:
      intro_turtle.goto(-60,-110)
    sys.stdout.flush()
sleep(1)
intro_turtle.clear()
next_word()
s.ontimer(update_countdown, t=1000)

    




def update_letter(correct_letter, letter_typed):
    global index
    global letter
    global cleared
    global words_typed
   
    # if the correct letter is the letter typed
    if correct_letter.lower() == letter_typed:
        if gameover == True:
            s.clear()
            s.bgpic('sky.gif')
        turtles[index].clear()
        turtles[index].color("plum")
        turtles[index].write(correct_letter, align="center", font=("Arial", 30, "normal"))
        index += 1

        # clear the existing text if word is done
        if index > len(string) - 1:
            for writer in turtles:
                writer.clear()
            turtles.clear() # clears the writers
            characters.clear() # clears the character list
            cleared = True
            words_typed += 1
            next_word()
        else:
            letter = characters[index]
            turtles[index].clear()
            turtles[index].color("blue")
            turtles[index].write(letter, align="center", font=("Arial", 30, "normal"))
            
    # if the correct letter is not the letter typed
    else:
        if gameover == True:
            s.clear()
            s.bgpic('sky.gif')
        turtles[index].clear()
        turtles[index].color("red")
        turtles[index].write(correct_letter, align="center", font=("Arial", 30, "normal", "underline", "bold"))


# function for updating each letter
def trigger_update_a():   
    update_letter(letter, "a")
    
def trigger_update_b():  
    update_letter(letter, "b")
    
def trigger_update_c():   
    update_letter(letter, "c")

def trigger_update_d():  
    update_letter(letter, "d")

def trigger_update_e():   
    update_letter(letter, "e")
    
def trigger_update_f():  
    update_letter(letter, "f")
    
def trigger_update_g():  
    update_letter(letter, "g")

def trigger_update_h():   
    update_letter(letter, "h")

def trigger_update_i():  
    update_letter(letter, "i")
    
def trigger_update_j():  
    update_letter(letter, "j")
    
def trigger_update_k():   
    update_letter(letter, "k")
    
def trigger_update_l():   
    update_letter(letter, "l")

def trigger_update_m():   
    update_letter(letter, "m")

def trigger_update_n(): 
    update_letter(letter, "n")
    
def trigger_update_o():  
    update_letter(letter, "o")
    
def trigger_update_p(): 
    update_letter(letter, "p")

def trigger_update_q():
    update_letter(letter, "q")

def trigger_update_r():  
    update_letter(letter, "r")
    
def trigger_update_s():  
    update_letter(letter, "s")
    
def trigger_update_t():  
    update_letter(letter, "t")

def trigger_update_u(): 
    update_letter(letter, "u")

def trigger_update_v(): 
    update_letter(letter, "v")
    
def trigger_update_w():  
    update_letter(letter, "w")
    
def trigger_update_x():  
    update_letter(letter, "x")

def trigger_update_y():  
    update_letter(letter, "y")

def trigger_update_z(): 
    update_letter(letter, "z")


# trigger the next letter with each letter of the alphabet
s.onkeypress(trigger_update_a, "a")
s.onkeypress(trigger_update_b, "b")
s.onkeypress(trigger_update_c, "c")
s.onkeypress(trigger_update_d, "d")
s.onkeypress(trigger_update_e, "e")
s.onkeypress(trigger_update_f, "f")
s.onkeypress(trigger_update_g, "g")
s.onkeypress(trigger_update_h, "h")
s.onkeypress(trigger_update_i, "i")
s.onkeypress(trigger_update_j, "j")
s.onkeypress(trigger_update_k, "k")
s.onkeypress(trigger_update_l, "l")
s.onkeypress(trigger_update_m, "m")
s.onkeypress(trigger_update_n, "n")
s.onkeypress(trigger_update_o, "o")
s.onkeypress(trigger_update_p, "p")
s.onkeypress(trigger_update_q, "q")
s.onkeypress(trigger_update_r, "r")
s.onkeypress(trigger_update_s, "s")
s.onkeypress(trigger_update_t, "t")
s.onkeypress(trigger_update_u, "u")
s.onkeypress(trigger_update_v, "v")
s.onkeypress(trigger_update_w, "w")
s.onkeypress(trigger_update_x, "x")
s.onkeypress(trigger_update_y, "y")
s.onkeypress(trigger_update_z, "z")

# listen for keyboard press and wait until user closes out of the tab
s.listen()
s.mainloop()

# Credit Sources

# cloud.gif:https://pngfree.io/cartoon-white-png-7259
# Ping2.wav:headspace.com
# sky.jpg:https://pngtree.com/freebackground/summer-landscape-vector-illustration-with-blue-sky-clouds-sun-green-meadow-flowers-and-trees-suitable-for-kids-background_1170497.html
