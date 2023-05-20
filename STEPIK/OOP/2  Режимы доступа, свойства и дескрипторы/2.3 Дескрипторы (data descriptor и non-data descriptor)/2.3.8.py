class StringValue:
    def __init__(self, min_length=2, max_length=50):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)

    def validate(self, string):
        if not (type(string) is str) or not (self.min_length <= len(string) <= self.max_length):
            return False
        return True


class PriceValue:
    def __init__(self, price=10000):
        self.price = price

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.name, value)

    def validate(self, string):
        if string <= self.price:
            return True
        return False


class Product:
    name = StringValue()
    price = PriceValue()

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class SuperShop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product: Product):
        self.goods.append(product)

    def remove_product(self, product: Product):
        self.goods.remove(product)


shop = SuperShop('Nike')
shop.add_product(Product('Airmax', 9500))
shop.add_product(Product('Jordan', 1270))
print(shop.name)
shop.goods[1].name = 123
print(shop.goods[1].name, shop.goods[1].price)