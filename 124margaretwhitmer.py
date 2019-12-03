import turtle as trtl

neb = trtl.Turtle()
neb.pensize(5)
neb.hideturtle()

line_length = 80
gap_size = 40

for i in range(26):
    neb.forward(line_length/2)
    neb.penup()
    neb.forward(gap_size)
    neb.pendown()
    neb.forward(line_length/2-gap_size)
    neb.left(90)
    #109.5
    line_length += 20

wn = trtl.Screen()
wn.mainloop()