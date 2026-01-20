# Section 1 - Your code
from utils import *
set_background("boxes (1)")

s1 = create_sprite("volleyball", 100, 100)
s2 = create_sprite("italy (1)", -100, 100)
s3 = create_sprite("korea", -100, -100)
s4 = create_sprite("snowboard", 150, -100)

message1 = create_sprite("alien",-200,230)
message1.color("hot pink")
message1.write("Nina",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("hot pink")
message2.write("bump, set, spike!",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()