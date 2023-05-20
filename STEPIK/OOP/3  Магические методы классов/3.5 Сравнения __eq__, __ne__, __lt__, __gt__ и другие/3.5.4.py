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
        return self.a * self.b * self.c

    def __lt__(self, other):
        return self.get_len() < other.get_len()

    def __le__(self, other):
        return self.get_len() <= other.get_len()


class ShopItem:
    def __init__(self, name: str, price: (int, float), dim: Dimension):
        self.name = name
        self.price = price
        self.dim = dim


snickers = ShopItem('Snickers', 1024, Dimension(40, 30, 120))
umbrella = ShopItem('Umbrella', 500, Dimension(10, 20, 50))
refrigerator = ShopItem('Refrigerator', 40000, Dimension(2000, 600, 500))
chairs = ShopItem('Chair', 2000, Dimension(500, 200, 200))

# print(snickers.dim.get_len())
lst = [snickers, umbrella, refrigerator, chairs]
lst_sorted = sorted(lst, key=lambda x: x.dim.get_len(), reverse=True)

for i in lst_sorted:
    print(i.name)