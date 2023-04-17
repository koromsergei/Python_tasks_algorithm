class RadiusVector2D:
    MIN_COORD = 0
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = x if self.check(x) else 0
        self.__y = y if self.check(y) else 0

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x if self.check(x) else self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y if self.check(y) else self.__y

    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2

    @classmethod
    def __check(cls, value):
        if type(value) in (int, float):
            if cls.MIN_COORD <= value <= cls.MAX_COORD:
                return True
        return False


v1 = RadiusVector2D()
v2 = RadiusVector2D(3, 4)
v3 = RadiusVector2D(-12, 2)

print(v2.x, v2.y)
v2.x = 14
print(v2.x)
print(v3.x)
print(RadiusVector2D.norm2(v1), RadiusVector2D.norm2(v2), RadiusVector2D.norm2(v3))
