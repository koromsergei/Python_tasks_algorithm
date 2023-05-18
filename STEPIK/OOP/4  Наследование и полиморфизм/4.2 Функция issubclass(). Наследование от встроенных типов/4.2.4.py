class Thing:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):
    def __init__(self, thing: Thing = None):
        if thing is None:
            super().__init__()
        else:
            self._type_check(thing)
            super().__init__({thing: (thing.name, thing.price, thing.weight)})

    def __setitem__(self, key, value: Thing):
        self._type_check(key)
        super().__init__({key: (value.name, value.price, value.weight)})

    @staticmethod
    def _type_check(key):
        if type(key) is Thing:
            return key
        else:
            raise TypeError


th = Thing('Cola', 69, 330)
th1 = Thing('Pepsi', 72, 330)
th2 = Thing('Fanta', 114, 900)

d = DictShop()
d[th] = th
d[th1] = th1
d[th2] = th2

# print(d.items())
d1 = DictShop(th)
print(d1.items())
