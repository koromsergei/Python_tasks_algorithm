class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        elif cls.count < 4:
            cls.count += 1
            cls.__instance = super().__new__(cls)
        elif cls.count >= 4:
            return cls.__instance
        return cls.__instance

    def __init__(self, name):
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
for i in objs:
    print(id(i))
