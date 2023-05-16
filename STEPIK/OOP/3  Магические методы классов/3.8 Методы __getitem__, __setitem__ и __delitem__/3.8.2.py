# class Record:
#     def __init__(self, **kwargs):
#         for i, j in kwargs.items():
#             setattr(self, i, j)
#
#     def __getitem__(self, item):
#         return
class Record:
    def __init__(self, pk=None, title=None, author=None):
        self.pk = pk
        self.title = title
        self.author = author

    def __getitem__(self, item):
        if item == 0:
            return self.pk
        if item == 1:
            return self.title
        if item == 2:
            return self.author

    def __setitem__(self, key, value):
        if key == 0:
            self.pk = value
        if key == 1:
            self.title = value
        if key == 2:
            self.author = value

r = Record(pk=1, title='21321', author=12312)

print(r[0])
