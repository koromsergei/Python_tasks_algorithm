import numpy as np


class PathLines:
    def __init__(self, *args):
        self._obj = list(args)

    def get_path(self):
        if len(self._obj) != 0:
            return self._obj
        else:
            return None

    def get_length(self):
        length = []
        for i, value in enumerate(self._obj):
            if i == 0:
                length.append(np.sqrt(value.x**2 + value.y**2))
                print(length[0])
            else:
                length.append(np.sqrt((value.x - self._obj[i - 1].x)**2 +
                              (value.y - self._obj[i - 1].y)**2))
        return sum(length)

    def add_lines(self, line):
        self._obj.append(line)


class LineTo:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = PathLines(LineTo(3, 4), LineTo(6, 8), LineTo(9, 12))
print(p.get_path())
print(p.get_length())
