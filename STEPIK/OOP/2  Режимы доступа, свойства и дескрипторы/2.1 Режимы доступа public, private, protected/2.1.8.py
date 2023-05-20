class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self):
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args):
        self.temp_tuple = args
        if len(self.temp_tuple) == 4:
            self.__x1, self.__y1, self.__x2, self.__y2 = self.temp_tuple
            self.__sp = Point(self.__x1, self.__y1)
            self.__ep = Point(self.__x2, self.__y2)
        else:
            self.__sp, self.__ep = self.temp_tuple

    def set_coords(self, sp: Point, ep: Point):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp.get_coords(), self.__ep.get_coords()

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


rec = Rectangle(1, 2, 3, 4)
rec1 = Rectangle(Point(11, 22), Point(33, 44))
pt = Point(111, 211)

rec.draw()
rec1.draw()
