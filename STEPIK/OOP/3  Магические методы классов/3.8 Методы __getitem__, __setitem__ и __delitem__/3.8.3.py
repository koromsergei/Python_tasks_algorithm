class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.points_list = []

    def add_point(self, x, y, speed):
        self.points_list.append([(x, y), speed])

    def __getitem__(self, item):
        try:
            return self.points_list[item]
        except IndexError:
            raise IndexError("Errror")

    def __setitem__(self, key, value):
        self.points_list[key][1] = value


tr = Track(10, -5)
tr.add_point(10, 0, 100)
tr.add_point(5, 3, 10)

cor, spe = tr[4]
print(cor)
tr[0] = 123
print(tr[0])
