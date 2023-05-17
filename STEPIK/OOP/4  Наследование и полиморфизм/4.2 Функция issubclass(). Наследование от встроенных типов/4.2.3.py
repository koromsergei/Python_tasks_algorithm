class ListInteger(list):
    def __init__(self, args):
        for i in args:
            self._check_value(i)
        super().__init__(args)

    def __setitem__(self, key, value):
        self._check_value(value)
        super().__setitem__(key, value)

    def append(self, i) -> None:
        self._check_value(i)
        super().append(i)

    @staticmethod
    def _check_value(i):
        if type(i) is not int:
            raise TypeError
        return i


lst = ListInteger((1, 2, 3))
print(lst)
lst[0] = 123
print(lst)
lst.append(1233)
print(lst)
