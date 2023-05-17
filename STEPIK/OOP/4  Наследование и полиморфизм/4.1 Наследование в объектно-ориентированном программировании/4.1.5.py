import random


class Things:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id = random.randint(0, 10000)
        self.dims = None
        self.weight = None
        self.memory = None
        self.firm = None

    def get_data(self):
        return self.name, self.price, self.id, self.dims, self.memory


class Table(Things):
    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Things):
    def __init__(self, id, name, price, memory, firm):
        super().__init__(name, price, id, memory, firm)


tb = Table('dadsa', 123, 12223, 1233)
print(tb.get_data())
