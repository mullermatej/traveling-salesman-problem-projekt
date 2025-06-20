import numpy as np


class City:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance(self, other: 'City') -> float:
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self) -> str:
        return f"City({self.x}, {self.y})"
