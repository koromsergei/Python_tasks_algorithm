class WindowDlg:
    def __init__(self):
        self.__title = 'Noname'
        self.__width = 100
        self.__height = 200

    def show(self):
        print(f'{self.__title}: {self.__width}, {self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if 0 <= width <= 10000:
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if 0 <= height <= 10000:
            self.__height = height
            self.show()


p = WindowDlg()
p.height = 1234
print(p.height)
