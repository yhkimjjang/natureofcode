import turtle
from walker05 import Walker

walker = Walker()

turtle.penup()
turtle.hideturtle()

while True:
    walker.step()
    turtle.goto(walker.getX(), walker.getY())
    turtle.dot(5, "blue")


