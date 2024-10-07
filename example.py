# ::: DON'T CHANGE ANYTHING IN LINES 2 - 7 :::
import turtle
t = turtle.Turtle()
t.shape("turtle")

# from svg_turtle import SvgTurtle
# t = SvgTurtle(400, 400)

# Type only your first name in the quotes below. No spaces!
first_name = "tulip"
# :::CREATE YOUR DRAWING BELOW:::
# a tulip
# base of the tulip
t.pensize(3)
t.right(90)
t.color("violet")
t.begin_fill()
t.circle(50, 180)

# petal starting from right side
t.forward(20)
t.left(15)
t.forward(50)
t.left(140)
t.forward(50)

# middle petal
t.right(130)
t.forward(50)
t.left(140)
t.forward(50)

# left petal
t.right(140)
t.forward(50)
t.left(140)
t.forward(50)
t.left(20)
t.forward(20)
t.end_fill()

# stem of tulip
t.goto(50, -50)
t.pensize(5)
t.color("green")
t.right(5)
t.forward(100)

# leaf
t.left(100)
t.begin_fill()
t.circle(80, 90)
t.left(90)
t.circle(80, 90)
t.end_fill()

# line inside the leaf
t.penup()
t.color("lightgreen")
t.goto(100, -75)
t.right(70)
t.pendown()
t.pensize(1)
t.circle(90, 55)
# t.hideturtle()


# ::: DON'T CHANGE ANYTHING BELOW THIS LINE:::
t.screen.mainloop() # keep the turtle window open
# svgturtle: save the drawing to an svg file:
# t.save_as(first_name + ".svg")