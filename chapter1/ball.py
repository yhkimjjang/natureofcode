import turtle
import random

class Ball:

    def __init__(self, width, height) -> None:
        self._width = width / 2
        self._heigh = height / 2

        self._x = 0
        self._y = 0
        
        self._directionX = 1
        self._directionY = 1

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
        self._ball.goto(self._x, self._y)

    def step(self) -> None:
        stepSize = random.uniform(0, 10)
        
        # x축의 방향 확인 후 step size 계산
        if self._directionX == 1 and (self._x + 20) > self._width:
            self._directionX = -1
        elif self._directionX == -1 and self._x < 0 and self._width - (abs(self._x) + 20) < 0:
            self._directionX = 1

        self._x += self._directionX * stepSize

        # y축의 방향 확인 후 step size 계산
        if self._directionY == 1 and (self._y + 30) > self._heigh:
            self._directionY = -1
        elif self._directionY == -1 and self._y < 0 and self._heigh - (abs(self._y) + 10) < 0:
            self._directionY = 1

        self._y += self._directionY * stepSize

