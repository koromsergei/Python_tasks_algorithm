class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify(value)
        setattr(instance, self.name, value)

    @classmethod
    def verify(cls, name):
        if type(name) is not float:
            raise TypeError(f'Type float is allowed, {type(name)} given')
        return True


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, n, m):
        self.cells = [[Cell().value for j in range(m)] for i in range(n)]


table = TableSheet(5, 3)
print(table.cells)
val = 1.0
for i in range(5):
    for j in range(3):
        table.cells[i][j] = val
        val += 1
print(table.cells)


