class RadiusVector:
    def __init__(self, *args):
        if len(args) > 1:
            self.vector = [*args]
        else:
            self.vector = [0 for i in range(args[0])]

    @property
    def vec(self):
        return self.vector

    @vec.setter
    def vec(self, *args):
        self.vector = [*args]

    def __len__(self):
        return len(self.vector)

    def __abs__(self):
        s = 0
        for i in self.vector:
            s += i**2
        return s


r = RadiusVector(1, 2, 3, 4)
r1 = RadiusVector(23)
print(abs(r))