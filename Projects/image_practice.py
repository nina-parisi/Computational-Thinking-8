# Section 1 - Your code
from utils import *
set_background("beach")

s1 = create_sprite("dolphin", 200, -100)
s2 = create_sprite("seashell", -200, -200)
s2 = create_sprite("turtle",  100, -150)
s2 = create_sprite("pineapple", -200, 200)

message1 = create_sprite("alien",-200,200)
message1.color("hot pink")
message1.write("Nina",font = ("georgia", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()