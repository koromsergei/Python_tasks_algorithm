def integer_params(func):
    def inner(self, *args, **kwargs):
        for i in args:
            print(i, type(i) is not int)
            if type(i) is not int:
                raise TypeError
        for i in kwargs.values():
            print(i, type(i) is not int)
            if type(i) is not int:
                raise TypeError
        return func(self, *args, **kwargs)
    return inner


def integer_params_decorated(cls):
    methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
    for k, v in methods.items():
        setattr(cls, k, integer_params_decorated(v))

    return cls


@integer_params
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def set_coords(self, *coords, reverse=False):
        c = list(coords)
        self.__coords = c if not reverse else c[::-1]


vector = Vector(1, 2)

vector[1] = 20.4
vector.set_coords(1, 2.3)
print(vector[1])
