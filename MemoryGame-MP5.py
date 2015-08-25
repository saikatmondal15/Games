# implementation of card game - Memory

import simplegui
import random


# helper function to initialize globals
def new_game():
    
    # Generate and shuffle a deck of cards
    global deck
    deck = range(8)+ range(8)
    random.shuffle(deck)
    
    # initialise a list of which cards are exposed
    global exposed
    exposed = []
    for card in deck:
        exposed.append(False)
        
    # reset turns to 0
    global turns
    turns =0
    
    # card_selected are the selected cards
    global card_selected
    card_selected=["",""]
    
    # state states the number of cards that have been chosen
    global state
    state = 0
          
    pass  

     
# define event handlers
def mouseclick(pos):
    global exposed
    global state
    global turns
    global card_selected
    global deck
    
    if state == 0:
        card_selected[0] = pos[0]//50 
        exposed[card_selected[0]]= True
        state = 1
        
    elif state == 1:
        if exposed[pos[0]//50]== False: #(If the card selected is unexposed)
            
            turns +=1
            card_selected[1] = pos[0]//50
            exposed[card_selected[1]]= True
            state = 2
        
    elif state == 2:
         if exposed[pos[0]//50]== False: #(If the card selected is unexposed)
            
            # if the selected cards don't match, unexpose them
            if deck[card_selected[0]] != deck[card_selected[1]]:
                exposed[card_selected[0]]=False
                exposed[card_selected[1]]=False
           
            card_selected[0]= pos[0]//50
            exposed[card_selected[0]]= True
            state = 1
        
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    for card_index in range(16):
        canvas.draw_text(str(deck[card_index]),[50*card_index+15,70],50, "White")
        
        if exposed[card_index]== False:
            card_vertices = ([card_index*50,0],[card_index*50,100],[card_index*50+50,100],[card_index*50+50,0]) 
            canvas.draw_polygon(card_vertices, 2, "Black", "Green")
   
    label.set_text("Turns = " + str(turns))
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



# Always remember to review the grading rubric