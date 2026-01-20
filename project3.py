import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -300
y1 = 100
x2 = -300
y2 = -100
x3 = -300
y3 = 200
x4 = -300
y4 = -200


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("track (1)")
t1 = create_sprite("basketball",x1,y1)
t2 = create_sprite("soccerball",x2,y2)
t3 = create_sprite("volleyball",x3,y3)
t4 = create_sprite("dodgeball",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# TODO - explain here which sprites are faster or slower
for i in range(30):
# x1 = basketball
    x1 += 8
# x2 = soccerball
    x2 += 10
# x3 = volleyball
    x3 += 20
# x4 = dodgeball
    x4 += 15
# volleyball is guaranteed to win because it is set at the fastest speed. 

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
    if x1 >= x2 and x1 >= x3 and x1 >= x4:
        print("basketball wins!")
    if x2 >= x1 and x2 >= x3 and x2 >= x4:
        print("soccer ball wins!")
    if x3 >= x1 and x3 >= x2 and x3 >= x4:
        print("volleyball wins!")
    if x4 >= x1 and x4 >= x2 and x4 >= x3:
        print("dodge ball wins!")


turtle.exitonclick()