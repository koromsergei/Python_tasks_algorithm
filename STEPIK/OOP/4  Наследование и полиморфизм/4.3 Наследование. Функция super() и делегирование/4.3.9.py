class StringDigit(str):
    def __init__(self, string):
        try:
            int(string)
            self.string = string
        except ValueError:
            raise ValueError('not int in string')

    def __add__(self, other):
        try:
            int(other)
            return StringDigit(self.string + other)
        except ValueError:
            raise ValueError('not str in string')


s = StringDigit('123')
d = StringDigit('322')
f = '213' + s
print(f)
