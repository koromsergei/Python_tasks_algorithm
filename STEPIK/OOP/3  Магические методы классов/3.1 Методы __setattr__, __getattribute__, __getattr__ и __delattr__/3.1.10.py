class Mechanical:
    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        super().__setattr__(key, value)


class Aragon:
    def __init__(self, date):
        self.date = date


class Calcium:
    def __init__(self, date):
        self.date = date


m = Mechanical(2023)
print(m.date)
