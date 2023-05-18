def integer_params(cls):
    def integer_params_decorated(*args):
        print(args)
        for i in args:
            print(i)
            if type(i) is not int:
                raise TypeError
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            print(k, v)
            setattr(cls, k, integer_params_decorated(v))

        return cls
    return integer_params_decorated


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
print(vector[1])
vector[1] = 20.4  # TypeError
