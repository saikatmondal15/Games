import random

# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

choice_list = [
    "rock",
    "Spock",
    "paper",
    "lizard",
    "scissors"
]

choice_map = {}

for num, choice in enumerate(choice_list):
    choice_map[choice] = num
    print choice_map

def name_to_number(name):
    return choice_map[name]

def number_to_name(number):
    return choice_list[number]
    
def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print
    
    # print out the message for the player's choice
    print 'Player chooses', player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(5)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses', comp_choice
    
    # compute difference of comp_number and player_number modulo five
    dif = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner, print winner message
    if dif == 0:
        print "Player and computer tie!"
    elif dif < 3:
        print "Player wins!"
    else:
        print "Computer wins!"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


