class Box:
    def __init__(self, name, max_weight):
        self._name = name
        self._max_weight = max_weight
        self._thing = list()

    @property
    def thing(self):
        return self._thing

    @thing.setter
    def thing(self, value):
        self._thing = value

    def add_thing(self, obj: tuple):
        self._thing.append(obj)
        if sum([i[1] for i in self._thing]) > self._max_weight:
            raise ValueError('превышен суммарный вес вещей')


class BoxDefender:
    def __init__(self, box: Box):
        self._box = box
        self._thing_t = box.thing[:]

    def __enter__(self):
        return self._box

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self._box.thing = self._thing_t
            raise Exception


box = Box("сундук", 1000)
box.add_thing(("спички", 46.6))
box.add_thing(("рубашка", 134))
box.add_thing(("стол", 134))

with BoxDefender(box) as b:
    b.add_thing((("стул", 134)))
    b.add_thing((("стульчик", 100)))

print(box._thing, 'box')
