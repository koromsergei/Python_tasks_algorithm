import numpy as np


class Params:
    MIN_DIMENSION = 1
    MAX_DIMENSION = 10000

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.verify(value):
            setattr(instance, self.name, value)

    @classmethod
    def verify(cls, value):
        return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION


class Dimension:
    a = Params()
    b = Params()
    c = Params()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_len(self):
        return np.sqrt(pow(self.a, 2) + pow(self.b, 2) + pow(self.c, 2))

    def __lt__(self, other):
        return self.get_len() < other.get_len()

    def __le__(self, other):
        return self.get_len() <= other.get_len()


d1 = Dimension(1, 2, 3)
d2 = Dimension(4, 5, 6)
print(d1 < d2)
