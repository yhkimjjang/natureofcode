import turtle
import random

class Ball:

    def __init__(self, width, height) -> None:
        self._width = width
        self._heigh = height

        self._x = 0
        self._y = 0

        self._ball = turtle.Turtle()
        self._ball.color('orange')
        self._ball.speed(0)
        self._ball.width(2)
        self._ball.hideturtle()
        self._ball.penup()
        self._ball.goto(-250, 0)
        self._ball.pendown()

    def _displayBall(self) -> None:
        self._ball.fillcolor('orange')
        self._ball.begin_fill()
        self._ball.circle(20)
        self._ball.end_fill()

    def moveBall(self) -> None:
        self._ball.clear()
        self._displayBall()
        self._ball.forward(0.5)

    def step(self) -> None:
        stepSize = random.uniform(0, 10)
        stepX = random.uniform(-stepSize, stepSize)
        stepY = random.uniform(-stepSize, stepSize)

        self._x += stepX
        if(self._x + 10) > self._width:
            stepX = random.uniform(-stepSize, 0)
            self._x += stepX
        if self._width - (self._x + 10) < 0:
            stepX = random.uniform(0, stepSize)
            self._x += stepX

