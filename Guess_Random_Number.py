"""Number Guessing Game"""

from random import * # importing random for the random number
from tkinter import * # importing tkinter for the gui

"""Main Gui Function"""
window = Tk() 
window.title("Number Guessing Game") # window name
window.config(background="black") # background of window

"""Gui Labels"""
Label (window, text= "For this Guessing Game you will enter a number between 1-100", bg="black", fg="white", font="none 12 bold").grid(row=1, column=0, sticky=N)
# add a label that shows previous guess

"""Gui Text"""
textentry = Entry(window, width=20, bg="white") # text input from user
textentry.grid(row=2, column=0, sticky=N) # location of text input
output = Text(window, width=40, height= 1, bg="white") # output button
output.grid(row=4, column=0, sticky=N) # location of output button

"""Funtions Gui"""
def click(): # function for the button submit
    entered_text = int(textentry.get())
    output.delete(0.0, END)
    guess = entered_text

    if guess > random_num: # if the input was greater than
        guess = ("Your guess was greater than the number")
        output.insert(END, guess)
    elif guess < random_num: # if the input was less than
        guess = ("Your guess was less than the number")
        output.insert(END, guess)
    elif guess == random_num: # if the input is correct
        guess = ("Congrats you got the number correct!")
        output.insert(END, guess)
    elif guess > 100: # if the input is outside the bounds
        guess = ("Guess was greater than 100")
        output.insert(END, guess)
    else: # if the input is outside the bounds
        if guess < 1:
            guess = ("Guess was less than 1")
            output.insert(END, guess)
        
def close_window(): # function that makes the exit button close the window
    window.destroy()
    exit()

"""Gui Buttons"""
Button(window, text="Submit", width=6, command=click).grid(row=3, column=0, sticky=N) # button for submitting an answer
Button(window, text="Exit", width=6, command=close_window).grid(row=8, column=0, sticky=N) # button for to close the window

"""Gui Dict"""
random_num = randint(1,100) # generates the randon number

"""Runs the window"""
window.mainloop() #calling the gui window