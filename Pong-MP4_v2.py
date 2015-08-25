# Implementation of classic arcade game Pong by Paula Alves

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    """initialize ball_pos and ball_vel"""
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [0, 0]
    
    """determine ball_vel"""
    if direction == RIGHT:
        ball_vel[0] = (random.randrange(120, 240) / 60) 
        ball_vel[1] = -(random.randrange(60, 80) / 60)
    else:
        ball_vel[0] = -(random.randrange(120, 240) / 60)
        ball_vel[1] = -(random.randrange(60, 80) / 60)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2 # these are ints
    paddle1_pos = HEIGHT/2 - PAD_HEIGHT/2 - 1
    paddle2_pos = HEIGHT/2 - PAD_HEIGHT/2 - 1
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0
    direction = random.choice([RIGHT, LEFT])
    spawn_ball(direction)

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    """ bounce ball off if it collides with either top or bottom wall"""
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    """ reflects ball if it hits paddles, spawn ball if it touches gutters"""
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] in range(paddle1_pos, paddle1_pos + PAD_HEIGHT + 1):
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH - 1 - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] in range(paddle2_pos, paddle2_pos + PAD_HEIGHT + 1):
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if HEIGHT - PAD_HEIGHT > paddle1_pos + paddle1_vel >= -1:
        paddle1_pos += paddle1_vel
#    print "1", paddle1_pos
    if HEIGHT - PAD_HEIGHT > paddle2_pos + paddle2_vel >= -1:
        paddle2_pos += paddle2_vel
#    print "2", paddle2_pos
      
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], 
                         [PAD_WIDTH, (paddle1_pos + PAD_HEIGHT)], 
                         [0, (paddle1_pos + PAD_HEIGHT)]], 1, "White", "White")
    canvas.draw_polygon([[WIDTH - PAD_WIDTH - 1, paddle2_pos], 
                         [WIDTH - 1, paddle2_pos], 
                         [WIDTH - 1, (paddle2_pos + PAD_HEIGHT)], 
                         [WIDTH - PAD_WIDTH - 1, (paddle2_pos + PAD_HEIGHT)]], 
                        1, "White", "White")

    # draw scores
    canvas.draw_text(str(score1), [140, 50], 40, "Yellow")
    canvas.draw_text(str(score2), [440, 50], 40, "Fuchsia")
    
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += 5
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= 5
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += 5
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= 5

 
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel, paddle2_vel = 0, 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background("Green")
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100) 


# start frame
new_game()
frame.start()
