import sys


class StreamData:
    def __init__(self):
        self.lst_values = None
        self.fields = None

    def create(self, fields: tuple, lst_values: list):
        if len(fields) != len(lst_values):
            return False

        for i, j in enumerate(fields):
            setattr(self, j, lst_values[i])

        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()