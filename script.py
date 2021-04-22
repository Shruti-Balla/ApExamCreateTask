#-----TYPING GAME NAME TBD-----

# import modules turtle, time, random, RandomWords
import turtle
import time
import random
from random_words import RandomWords

s = turtle.Screen()
s.setup(600,600)
s.bgpic('sky.gif')

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

print(initial_x, initial_y)
# begin game - make the first letter blue
def begin_game():
    global index
    global letter
    global cleared

    index = 0
    turtles[0].clear()
    turtles[0].color("blue")
    turtles[0].write(characters[0], align="center", font=("Arial", 30, "normal", "underline"))
    letter = characters[0]
    cleared = False



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
seconds = 120

def update_countdown():
    global seconds
    timer_turtle.clear()
    timer_turtle.write(str(seconds), font=("Times New Roman", 30, "normal"))
    seconds -= 1
    if seconds == 0:
        pass # Trigger Game Over screen
    else:
        s.ontimer(update_countdown, t=1000)

    

# create a timer - CHANGE IT!!!!!!!!!!
s.ontimer(update_countdown, t=1000)
    

# puts writers and characters at corresponding indexes
def initialize(new_string):
    global string
    global initial_x
    global initial_y
    global index

    index = 0

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
        writer.goto(initial_x, initial_y) # change location
        writer.write(characters[index], align="center", font=("Arial", 30, "normal"))
        index += 1
        initial_x += 25
    initial_x = random.randint(-300, 10)
    initial_y = random.randint(-300, 10)
    begin_game() # writes word
    


def update_letter(correct_letter, letter_typed):
    global index
    global letter
    global cleared
    global 
   
    # if the correct letter is the letter typed
    if correct_letter.lower() == letter_typed:
        turtles[index].clear()
        turtles[index].color("green")
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
        turtles[index].clear()
        turtles[index].color("red")
        turtles[index].write(correct_letter, align="center", font=("Arial", 30, "normal", "underline", "bold"))

# move on to the next word in the list
i = 0
def next_word():
    global i
    while cleared:
        print(cleared)
        initialize(strings[i])
        i += 1

next_word()

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
