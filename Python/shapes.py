from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:
sides= input('Please enter a value')
color=input('What color?')
size=input('How big? Enter a numerical value')
sizea=int(size)
#user input for sides is stored as variable sides
#user input for color is stored as color
#user input for size is stored as size
t.color(color)
t.begin_fill()
for i in range(int(sides)):
    t.pendown()
    t.pencolor(color)
    t.forward(sizea*10)
#360/x is the formula for exterior angles of an "x" sided polygon
    t.right(360/int(sides))
t.end_fill()
# Close window on click.
exitonclick()
