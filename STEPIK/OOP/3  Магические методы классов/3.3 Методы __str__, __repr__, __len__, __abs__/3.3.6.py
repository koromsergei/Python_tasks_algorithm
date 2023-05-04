class Complex:
    def __init__(self, real_value=0, img_value=0):
        self.real_value = real_value
        self.img_value = img_value

    @property
    def real(self):
        return self.real_value

    @real.setter
    def real(self, value):
        self.real_value = value
        if type(value) in (int, float):
            self.real_value = value
        else:
            raise ValueError()

    @property
    def img(self):
        return self.img_value

    @img.setter
    def img(self, value):
        if type(value) in (int, float):
            self.img_value = value
        else:
            raise ValueError()

    def __abs__(self):
        return (self.real_value * self.real_value) + (self.img_value * self.img_value)


cmp = Complex(1, 2)
print(abs(cmp))

