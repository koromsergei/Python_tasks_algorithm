class Lst:
    def __init__(self, lst):
        self.lst = lst

    def __sub__(self, other):
        for i in other.lst:
            if i in self.lst:
                self.lst.remove(i)
        return self.lst


l = Lst([1, 2, 3, 4, 5, 6])
l1 = Lst([4, 5, 6])

print(l - l1)
