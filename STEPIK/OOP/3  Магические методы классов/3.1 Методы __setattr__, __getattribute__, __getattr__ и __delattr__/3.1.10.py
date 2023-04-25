import time

class Mechanical:
    date = None

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if self.date is None:
            super().__setattr__(key, value)


class Aragon:
    date = None

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if self.date is None:
            super().__setattr__(key, value)


class Calcium:
    date = None

    def __init__(self, date):
        self.date = date

    def __setattr__(self, key, value):
        if self.date is None:
            super().__setattr__(key, value)


class GeyserClassic:
    MAX_DATE_FILTER = 100

    def __init__(self):
        self.filter_dict = {1: None, 2: None, 3: None}

    def add_filter(self, slot_num: int, filter):
        if self.filter_dict[slot_num] is None:
            if slot_num == 1 and isinstance(filter, Mechanical):
                self.filter_dict[slot_num] = filter
            if slot_num == 2 and isinstance(filter, Aragon):
                self.filter_dict[slot_num] = filter
            if slot_num == 3 and isinstance(filter, Calcium):
                self.filter_dict[slot_num] = filter

    def remove_filter(self, slot_num):
        self.filter_dict.pop(slot_num)

    def get_filters(self):
        return self.filter_dict.items()

    def water_on(self):
        for i in range(1, 4, 1):
            if self.filter_dict[i] is None:
                return False
            if not (0 <= time.time() - self.filter_dict[i].date <= self.MAX_DATE_FILTER):
                return False
        return True


water = GeyserClassic()
water.add_filter(1, Mechanical(time.time()))
water.add_filter(2, Aragon(time.time()))
water.add_filter(3, Calcium(time.time()))

print(water.get_filters())
print(water.water_on())
