class Model:
    def __init__(self):
        self.id = None
        self.fio = None
        self.old = None

    def query(self, id: int, fio: str, old: int):
        self.id = id
        self.fio = fio
        self.old = old

    def __str__(self):
        if self.id is not None:
            return f'Model: id = {self.id}, fio = {self.fio}, old = {self.old}'
        else:
            return 'Model'


m = Model()
m.query(1, 's', 12)
print(m)


