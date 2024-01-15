import turtle

class Ball:

    def __init__(self, width, height) -> None:
        self._x = 0
        self._y = 0
        self._xspeed = 1
        self._yspeed = 3.3

        self._maxWidth = width /2
        self._minWidth = -self._maxWidth

        self._maxHeight = height / 2
        self._minHeight = -self._maxHeight

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
        self._x += self._xspeed
        self._y += self._yspeed

        if self._x < self._minWidth or self._x > self._maxWidth:
            self._xspeed *= -1

        if self._y < self._minHeight or self._y > self._maxHeight:
            self._yspeed *= -1