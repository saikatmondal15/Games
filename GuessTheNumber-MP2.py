# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math


# initialize global variables used in your code
num_range = 100


# helper function to start and restart the game
def new_game():
    # remove this when you add your code    
    global secret_number, num_range
    secret_number = random.randrange(0, num_range)
    print
#    print secret_number
    print "New game!"
    print "Guess the number between 0 and less than", num_range
  
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    new_game()

    
def input_guess(guess):
    # main game logic goes here
    global player_guess, secret_number
    player_guess = int(guess)
    print "Your guess was:", player_guess
    if player_guess > secret_number:
        print "Lower!"
    elif player_guess < secret_number:
        print "Higher!"
    elif player_guess == secret_number:
        print "Correct!"
        new_game()
    else:
        print "Error"
    
    
# create frame
frame = simplegui.create_frame("Guess the number!", 300, 250)


# register event handlers for control elements
frame.add_button("Range (0-100]", range100, 70)
frame.add_button("Range (0-1000]", range1000, 70)
frame.add_input("Enter your guess", input_guess, 70)


# call new_game and start frame
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
