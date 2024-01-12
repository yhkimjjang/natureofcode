import turtle
from ball import Ball

screenWidth = 800
screenHeigh = 400

screen = turtle.Screen() 
screen.setup(screenWidth, screenHeigh)
screen.tracer(0)

ball = Ball(screenWidth, screenHeigh)

while True:
    ball.moveBall()
    screen.update()
