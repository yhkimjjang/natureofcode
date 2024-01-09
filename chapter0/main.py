from turtle import *
from random import random
from walker import Walker

t = Turtle()
t.penup()
t.hideturtle()

walker = Walker()

while True:
    walker.step()
    t.goto(walker.getXPosition(), walker.getYPosition())
    t.dot(5, "blue")

t.screen.mainloop()