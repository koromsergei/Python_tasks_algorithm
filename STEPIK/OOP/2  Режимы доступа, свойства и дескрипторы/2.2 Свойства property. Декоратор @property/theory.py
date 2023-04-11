class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    def get_old(self):
        return self.__old

    def set_old(self, old):
        self.__old = old

    def del_old(self):
        del self.__old

    old = property(get_old, set_old, del_old)


p = Person('sergei', 25)
p.__height = 188
print(p.old)
print(p.old)
del p.old
print(p.__dict__)
p.__dict__['__height'] = 1
print(p.__dict__)
