class PVector:

    def __init__(self, x, y) -> None:
        self._x = x
        self._y = y

    def getX(self):
        return self._x
    
    def getY(self):
        return self._y

    def add(self, vector: PVector) -> None:
        self._x += vector.getX()
        self._y += vector.getY()