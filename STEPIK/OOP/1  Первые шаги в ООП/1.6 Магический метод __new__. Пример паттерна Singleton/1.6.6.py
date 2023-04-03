class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return "Error. New class initialization is prohibited"


ob = AbstractClass()
print(ob)
