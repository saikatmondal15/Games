# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0
x = 0
y = 0


# define helper functions that converts time
# in tenths of seconds into formatted string A:BC.D
      
def format_time(t):
    """ this helper function converts time into formatted string"""
    minutes = str(t // 600)
    milisec = str(t % 10)
    seconds = (t // 10) % 60

    if seconds < 10:
        return minutes + ":0" + str(seconds) + "." + milisec   
    else:
        return minutes + ":" + str(seconds) + "." + milisec


# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()


def stop():
    global x, y, status
    status = timer.is_running()
    if status == True:
        timer.stop()
        y += 1
        if (t % 10) == 0:
            x += 1
    return x, y
        

def reset():
    global t, x, y
    timer.stop()
    t = x = y = 0
    return x, y


# define event handler for timer with 0.1 sec interval
def time_handler():
    global t
    t += 1
    return t

# define draw handler
def draw(canvas):
    canvas.draw_text(format_time(t), (70, 170), 70, "Red")
    canvas.draw_text(str(x) + "/" + str(y), (230, 40), 35, "White")

    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, time_handler)

# start frame
frame.start()
