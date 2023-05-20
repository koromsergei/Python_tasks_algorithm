from random import randint


class Product:
    data_types = {'name': str,
                  'weight': (float, int),
                  'price': (float, int),
                  'id': int}

    def __init__(self, name: str, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
        self.id = randint(1, 1000000)

    def __setattr__(self, key, value):
        if isinstance(value, (self.data_types[key])):
            super().__setattr__(key, value)
        else:
            raise TypeError("Error in type")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError('id can`t be deleted')

class Shop:
    def __init__(self, chanel_name):
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)




p = Product('test prod', 21, 12)
del p.name

