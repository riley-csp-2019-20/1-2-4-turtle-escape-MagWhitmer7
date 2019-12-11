import turtle as trtl
import random

# create drawer turtle
neb = trtl.Turtle()
neb.pensize(5)
neb.hideturtle()

# create player turtle
player = trtl.Turtle()
player.turtlesize(2)
player.setheading(90)
player.pencolor("darkmagenta")
player.penup()
player.goto(-80, 80)


# define variables for use in for loop
line_length = 80 # size of the maze line, changes
gap_size = 40 # size of the gap, static
wall_width = 40 # size of the barrier, static

# def's 
def draw_door():
  neb.penup()
  neb.forward(gap_size) # make the gap
  neb.pendown()

def draw_barrier():
  neb.left(90) # turn left
  neb.forward(wall_width) # draw barrier
  neb.back(wall_width) # go back to the maze line
  neb.right(90)

def up():
  player.setheading(90)
  player.forward(10)

def down():
  player.setheading(270)
  player.forward(10)

def left():
  player.left(90)
  player.forward(10)

def right():
  player.right(90)
  player.forward(10)

# create maze
for i in range(26):
  if (i > 4):
    door = random.randint(gap_size, line_length-2*gap_size) # controls where the gap is
    barrier = random.randint(2*wall_width, line_length-2*gap_size) # controls where the barrier is
    if (door < barrier):
      # draw door
      neb.forward(door)  # go to door beginning
      draw_door()
  
      # draw barrier
      neb.forward(barrier - door - gap_size) # move past the gap a set number
      draw_barrier()
            
      # finish wall
      neb.forward(line_length - barrier)
            
    else:
      # draw barrier
      neb.forward(barrier) # move past the gap a set number
      draw_barrier()

      # draw door
      neb.forward(door - barrier)
      draw_door()

      # finish wall
      neb.forward(line_length - door - gap_size)       
  
  neb.left(90) # turn to draw the next maze line
  #109.5
  line_length += 20 # increase the line size to create a spiral

wn = trtl.Screen()
wn.onkeypress(up, "up")
wn.onkeypress(down, "down")
wn.onkeypress(left, "left")
wn.onkeypress(right, "right")
wn.mainloop()
