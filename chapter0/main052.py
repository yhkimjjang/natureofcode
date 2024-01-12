import turtle
from walker052 import Walker

walker = Walker(-400, 0)

turtle.penup()
turtle.hideturtle()

while True:
    walker.step()
    turtle.goto(walker.getX(), walker.getY())
    turtle.dot(3, "blue")
