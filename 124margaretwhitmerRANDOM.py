import turtle as trtl
import random

# create turtle
neb = trtl.Turtle()
neb.pensize(5)
neb.hideturtle()

# define variables for use in for loop
line_length = 80 # size of the maze line, changes
gap_size = 40 # size of the gap, static
wall_width = 45 # size of the barrier, static

# create maze
for i in range(26):
    # Create randomly generated variable numbers to move the 
    # barriers and gaps to different places
    gap_placement = random.randint() # controls where the gap is
    barrier_spacing = random.randint() # controls where the barrier is
    # create first half of line and gap
    neb.forward(gap_placement) # move forward halfway
    neb.penup()
    neb.forward(gap_size) # make the gap
    neb.pendown()
    # create barriers
    if i > 4:
        neb.forward(barrier_spacing) # move past the gap a set number
        neb.left(90) # turn left
        neb.forward(wall_width) # draw barrier
        neb.back(wall_width) # go back to the maze line
        neb.right(90) # turn right to continue drawing the maze
    # finish maze line after gaps and barriers created
    neb.forward(line_length/2-gap_size) # draw the second half of the line, calculating out the gap size
    neb.left(90) # turn to draw the next maze line
    #109.5
    line_length += 20 # increase the line size to create a spiral

wn = trtl.Screen()
wn.mainloop()