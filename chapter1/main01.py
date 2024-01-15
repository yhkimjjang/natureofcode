import turtle
# from ball import Ball
from ball02 import Ball

screenWidth = 800
screenHeigh = 400

screen = turtle.Screen() 
screen.setup(screenWidth, screenHeigh)
screen.tracer(1, 1)

ball = Ball(screenWidth, screenHeigh)

while True:
    ball.step()
    ball.moveBall()
    screen.update()
