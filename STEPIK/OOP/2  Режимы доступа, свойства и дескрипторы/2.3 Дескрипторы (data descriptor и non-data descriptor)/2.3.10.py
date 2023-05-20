class DataTelecast:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Telecast:
    id = DataTelecast()
    name = DataTelecast()
    duration = DataTelecast()

    def __init__(self, id: int, name: str, duration: int):
        self.id = id
        self.name = name
        self.duration = duration


class TVProgram:
    def __init__(self, chanel_name):
        self.chanel_name = chanel_name
        self.items = []

    def add_telecast(self, tl: Telecast):
        self.items.append(tl)

    def remove_telecast(self, indx):
        self.items.pop(indx)


pr = TVProgram('Euronews')
pr.add_telecast(Telecast(1, 'Morning!', 1000))
pr.add_telecast(Telecast(2, 'No comments', 30))
print(pr.items[0].__dict__)
print(pr.__dict__)
