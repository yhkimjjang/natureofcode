from random import random

class Walker:
    def __init__(self) -> None:
        self._x = 0
        self._y = 0
        self._stepValue = 2

    def getXPosition(self):
        return self._x
    
    def getYPosition(self):
        return self._y
    
    def step(self):
        stepX = int(random() * 3) - 1
        stepY = int(random() * 3) - 1

        self._x += (stepX * self._stepValue)
        self._y += (stepY * self._stepValue)