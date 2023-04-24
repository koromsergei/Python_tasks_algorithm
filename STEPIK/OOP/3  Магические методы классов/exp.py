class A:
    def __init__(self, a):
        self.__a = a

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value


ad = A(12)
print(ad.a)