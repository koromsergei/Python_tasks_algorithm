class Cart:
    def __init__(self, goods=None):
        if goods is None:
            goods = []
        self.goods = goods

    def add_goods(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return self.goods


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add_goods(TV('Samsung', 1000))
cart.add_goods(TV('LG', 2000))
cart.add_goods(TV('Samsung', 1100))
cart.add_goods(TV('LG', 2120))
cart.add_goods(Notebook('noname', 11))
cart.add_goods(Table('noname', 120))
cart.add_goods(Cup('Lol', 12))
print(cart.get_list()[2].name)



