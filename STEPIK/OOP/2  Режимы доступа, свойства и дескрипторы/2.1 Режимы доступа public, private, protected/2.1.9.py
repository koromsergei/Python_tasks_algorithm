class LinkedList:
    def __init__(self):
        self.__obj = []
        self.head = self.__obj[0] if len(self.__obj) != 0 else None
        self.tail = self.__obj[-1] if len(self.__obj) != 0 else None

    def add_obj(self, obj):
        self.__obj.append(obj)

    def remove_obj(self):
        self.__obj.pop()

    def get_data(self):
        return [i.get_data() for i in self.__obj]


class ObjList:
    def __init__(self, data: str):
        self.__data = data
        self.__next = None
        self.__prev = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next.get_data()

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj


lst = LinkedList()
obj1 = ObjList('data 1')
obj2 = ObjList('data 2')
obj3 = ObjList('data 3')
obj4 = ObjList('data 4')

lst.add_obj(obj1)
lst.add_obj(obj2)
lst.add_obj(obj3)
lst.add_obj(obj4)

obj1.set_next(obj2)
obj2.set_next(obj3)
obj3.set_next(obj4)

obj2.set_prev(obj1)
obj3.set_prev(obj2)
obj4.set_prev(obj3)

print(obj2.get_next())
print(lst.get_data())
