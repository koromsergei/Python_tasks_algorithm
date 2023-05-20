class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old

    def pr(self):
        print('dsad')


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        print('Cat', self.name, self.old, self.color, self.weight)


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        print('Dog', self.name, self.old, self.breed, self.size)


cat = Cat('Car', 4, 'sad', 2)
cat.pr()
cat.get_info()


