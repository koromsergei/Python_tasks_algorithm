from abc import abstractmethod


class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super(ShopItem, self).__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    def __init__(self):
        super(ShopGenericView, self).__init__()

    def __str__(self):
        res = list(zip(self.__dict__.keys(), self.__dict__.values()))
        print(str(res))
        # res = str(self.__dict__.items())
        return f'{list(zip(self.__dict__.keys()))}: {self.__dict__.values()}'
        # return res


class Book(ShopItem, ShopGenericView):
    def __init__(self, title, author, year):
        super(Book, self).__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
