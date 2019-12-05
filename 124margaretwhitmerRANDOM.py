import turtle as trtl
import random as rand

neb = trtl.Turtle()
neb.pensize(5)
neb.hideturtle()

line_length = 80
gap_size = 40
wall_width = 45
barrier_spacing = 10

for i in range(26):
    neb.forward(line_length/2)
    neb.penup()
    neb.forward(gap_size)
    neb.pendown()
    if i > 4:
        neb.forward(barrier_spacing)
        neb.left(90)
        neb.forward(wall_width)
        neb.back(wall_width)
        neb.right(90)
        barrier_spacing += 4
    neb.forward(line_length/2-gap_size)
    neb.left(90)
    #109.5
    line_length += 20

wn = trtl.Screen()
wn.mainloop()