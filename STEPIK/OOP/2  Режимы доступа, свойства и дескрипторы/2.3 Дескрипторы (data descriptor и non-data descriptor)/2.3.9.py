class Descr_Thing:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Thing:
    thing_name = Descr_Thing()
    weight = Descr_Thing()

    def __init__(self, thing_name: str, weight):
        self.thing_name = thing_name
        self.weight = weight


class Bag:
    t = Thing('Nike', 213)

    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.__things = []
        self.t = str(max_weight) + 'dsd'

    @property
    def things(self):
        return self.__things

    def add_thing(self, thing: Thing):
        if sum([i.weight for i in self.__things]) + thing.weight <= self.max_weight:
            self.__things.append(thing)

    def remove_thing(self, indx):
        self.__things.pop(indx)

    def get_total_weight(self):
        return sum(self.__things)


bag = Bag(1000)
bag.add_thing()
print(Bag.things[0].weight)