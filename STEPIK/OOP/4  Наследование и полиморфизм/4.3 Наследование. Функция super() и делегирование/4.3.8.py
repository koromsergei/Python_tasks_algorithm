class SoftList(list):
    def __init__(self, lst=None):
        super().__init__(lst)

    def __getitem__(self, item):
        try:
            res = super().__getitem__(item)
            return res
        except IndexError:
            return False


lst = SoftList((1, 2, 3, 4))
print(lst[2])