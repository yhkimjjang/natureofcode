from noise import pnoise1

class Walker:
    def __init__(self, x, y) -> None:
        self._step = 1
        self._t = 0.1
        self._x = x
        self._y = y

    def step(self):
        n = pnoise1(self._t)
        self._y = self._y + (n * self._step)
        self._x += self._step
        self._t += 0.1

    def getX(self):
        return self._x

    def getY(self):
        return self._y
