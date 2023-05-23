from abc import abstractmethod, ABC
from random import randint


class ShopInterface(ABC):
    @abstractmethod
    def get_id(self):
        print('sd')


class ShopItem(ShopInterface):
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = randint(0, 100000)

    def get_id(self):
        return self.__id


r = ShopItem('sad', 21, 123)
print(r.get_id())
