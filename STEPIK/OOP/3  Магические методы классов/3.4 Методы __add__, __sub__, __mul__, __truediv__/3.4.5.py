class ListMath:
    def __init__(self, lst):
        if lst is None:
            self.lst_math = []
        else:
            self.lst_math = [i for i in lst if type(i) in (int, float)]

    def __add__(self, other):
        return [i + other for i in self.lst_math]

    def __radd__(self, other):
        return self + other


l = ListMath([1, 2, 3, 4, 5, 6])
t = l + 2
k = 2 + l

print(k)
