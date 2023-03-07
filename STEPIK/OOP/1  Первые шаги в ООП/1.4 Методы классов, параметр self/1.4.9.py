import sys

# lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
lst_in = ['1 Сергей 35 1200000', '2 Иван 25 120000', '1 Николай 5 1200000']


class DataBase:
    FIELDS = ('id', 'name', 'old', 'salary')

    def __init__(self):
        self.lst_data = []

    def get_data(self, a: int, b: int):
        if b > len(self.lst_data):
            b = self.lst_data
        return self.lst_data[a:b + 1]

    def set_data(self, data):
        for i in data:
            self.lst_data.append({self.FIELDS[ind]: val for ind, val in enumerate(i.split())})


db = DataBase()
db1 = DataBase()
db.set_data(lst_in)
print(db.get_data(0, 1))
