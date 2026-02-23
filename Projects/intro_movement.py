import time, turtle, random
from utils import *
# Section 1: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)
s2 = create_sprite("basketball", 0,0)

# Section 2: define controls
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 10
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 10
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 10
    y = s1.ycor() 
    s1.goto(x,y)
    
def move_right(): 
    x = s1.xcor() + 10
    y = s1.ycor() 
    s1.goto(x,y)

def draw ():
    s1.pendown()
def stop_drawing():
    s1.penup()
def erase(): 
    s1.clear()
def red_pen():
    s1.color("red")
def green_pen():
    s1.color("green")
def reset ():
    s1.goto(0,0)


window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_right, "d")
window.onkeypress(move_left, "a")
window.onkeypress(draw, "c")
window.onkeyrelease(stop_drawing, "c")
window.onkeypress(erase, "e")
window.onkeypress(red_pen,"r")
window.onkeypress(green_pen,"g")
window.onkeypress(reset," ")

#movement code for s2
def move_up():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)
    
def move_left():
    x = s2.xcor() - 10
    y = s2.ycor() 
    s2.goto(x,y)
    
def move_right(): 
    x = s2.xcor() + 10
    y = s2.ycor() 
    s2.goto(x,y)

def reset ():
    s2.goto(0,0)



window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_right, "Right")
window.onkeypress(move_left, "Left")
window.onscreenclick(reset,"x,y")



# Section 3: define other controls
def hide():
    s1.hideturtle()
def show():
    s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")



# Section 4: game loop
window.listen()
for i in range(1000000000):
    time.sleep(0.01)
    window.update()