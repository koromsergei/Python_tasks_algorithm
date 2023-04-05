class A:
    def __init__(self):
        self._x = 12

    @property
    def x(self):
        return 100

a = A()
print(a.x)
a.x = 1132