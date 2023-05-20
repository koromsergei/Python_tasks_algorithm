class Point:
    color = 'red'
    circle = 2

    def __init__(self):
        self.x = 2
        self.y = 2
        self.color = 'red'

    def set_coords(self, x, y):
        self.color = 'blue'
        self.x = x
        self.y = y

    def get_coord(self):
        print(self.x, self.color)


p1 = Point()
print(p1.x)
p1.get_coord()
p1.set_coords(1, 2)
p1.get_coord()
p2 = Point()
p2.set_coords(2, 3)
print(p1.__dict__)
print(p2.__dict__)
