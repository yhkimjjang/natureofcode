from random import random

class Walker:
    def __init__(self) -> None:
        self._x = 0
        self._y = 0
        self.stuff = [1, 2, 3, 4, 4]

    def step(self):
        index = int(random() * 5)
        value = self.stuff[index]

        if value == 1:
            self._y += 2
        elif value == 2:
            self._y -= 2
        elif value == 3:
            self._x -= 2
        else:
            self._x += 2

    def jump(self, x, y):
        jumpRating = random()
        if jumpRating < 0.5:
            self._x = x
            self._y = y

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y