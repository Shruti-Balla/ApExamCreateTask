import turtle
from time import time
import random
from random_words import RandomWords

# initialize variables
rw = RandomWords()
words = rw.random_words(count=4)
turtles = []
#string = "the quick brown fox jumps over the lazy dog."
strings = words
random.shuffle(strings)
characters = []
index = 0
initial_x = -275
initial_y = 50
letter = ""
letters_typed = 0





# begin game - make the first letter blue
def begin_game():
    global index
    global letter

    index = 0
    turtles[0].clear()
    turtles[0].color("blue")
    turtles[0].write(characters[0], align="center", font=("Arial", 30, "normal", "underline"))
    letter = characters[0]

# puts writers and characters at corresponding indexes
for string in strings:
    index = 0
    for character in string:
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
        '''if index == 30:
            initial_y = -50
            initial_x = -125
        else:'''
        initial_x += 20
    begin_game()
    characters.clear()
    turtles.clear()

def update_letter(correct_letter, letter_typed):
    global index
    global letters_typed
    global letter

    # if the character is not a letter, lower() won't work
    try:
        
        # if the correct letter is the letter typed
        if correct_letter.lower() == letter_typed:
            turtles[index].clear()
            turtles[index].color("green")
            turtles[index].write(correct_letter, align="center", font=("Arial", 30, "normal"))
            letters_typed += 1
            index += 1

            # clear the existing text
            if index > len(string) - 1:
                for writer in turtles:
                    writer.clear()
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
            letters_typed += 1

    except:

        # if the correct letter is the letter typed
        if correct_letter == letter_typed:
            turtles[index].clear()
            turtles[index].color("green")
            turtles[index].write(correct_letter, align="center", font=("Arial", 30, "normal"))
            letters_typed += 1
            index += 1
            if index > len(string) - 1:
                for writer in turtles:
                    writer.clear()
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
            letters_typed += 1


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

def trigger_update_space(): 
    update_letter(letter, " ")

def trigger_update_period(): 
    update_letter(letter, ".")


s = turtle.Screen()
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
s.onkeypress(trigger_update_space, " ")
s.onkeypress(trigger_update_period, ".")
s.listen()
s.mainloop()
