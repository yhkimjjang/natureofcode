import random
import math

class Walker:
    def __init__(self) -> None:
        self._x = 0
        self._y = 0

    def step(self):
        # stepSize = random.uniform(0, 16)
        stepSize = self._montecarlo()
        # print(stepSize)

        stepX = random.uniform(-stepSize, stepSize)
        stepY = random.uniform(-stepSize, stepSize)

        self._x += stepX
        self._y += stepY

    def getX(self):
        return self._x

    def getY(self):
        return self._y
    
    def _montecarlo(self):
        while True:
            r1 = math.pow(random.uniform(0, 4), 2)
            probability = r1
            r2 = math.pow(random.uniform(0, 4), 2)
            if r2 < probability:
                return r1