class Person:
    def __init__(self, fio: str, job: str, old: int, salary: int, year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._attr_lst = list(self.__dict__)
        self._attr = self.__dict__

    def __getitem__(self, item):
        try:
            return self._attr[self._attr_lst[item]]
        except IndexError:
            raise IndexError('Wrong index')

    def __setitem__(self, key, value):
        try:
            setattr(self, self._attr_lst[key], value)
        except IndexError:
            raise IndexError('Wrong index')

    def __next__(self):
        if len(self._attr_lst) != 0:
            return self._attr_lst.pop(0)
        else:
            raise StopIteration

    def __iter__(self):
        return self


pr = Person('Sergei', 'IT', 23, 213, 2022)

for i in pr:
    print(i)
