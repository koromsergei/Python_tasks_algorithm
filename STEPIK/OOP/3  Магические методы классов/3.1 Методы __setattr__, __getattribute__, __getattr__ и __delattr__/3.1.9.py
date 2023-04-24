class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 100

    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value if self.verify(value) else self.__a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value if self.verify(value) else self.__b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        self.__c = value if self.verify(value) else self.__c

    @classmethod
    def verify(cls, value):
        if cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION:
            return True
        return False

    def __setattr__(self, key, value):
        if key == self.MIN_DIMENSION or key == self.MAX_DIMENSION:
            raise AttributeError('No')
        else:
            super().__setattr__(key, value)

d = Dimensions(23, 20, 45)

print(d.a)
d.a = 123
print(d.a)

d.MIN_DIMENSION = 123
print(d.MIN_DIMENSION)
