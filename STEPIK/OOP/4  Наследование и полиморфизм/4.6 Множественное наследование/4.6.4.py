class Digit:
    def __init__(self, value):
        self.value = value


class Integer(Digit):
    def __init__(self, value):
        if type(value) is int:
            super(Integer, self).__init__(value)
        else:
            raise TypeError


class Float(Digit):
    def __init__(self, value):
        if type(value) is float:
            super(Float, self).__init__(value)
        else:
            raise TypeError


class Positive(Digit):
    def __init__(self, value):
        if value > 0:
            super(Positive, self).__init__(value)
        else:
            raise TypeError


class Negative(Digit):
    def __init__(self, value):
        if value < 0:
            super(Negative, self).__init__(value)
        else:
            raise TypeError


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super(PrimeNumber, self).__init__(value)


class FloatNumber(Integer, Positive):
    def __init__(self, value):
        super(FloatNumber, self).__init__(value)


i = PrimeNumber(213)

print(i.value)
