# здесь объявляются все необходимые классы

# считывание списка из входного потока (эту строку не менять)
# data_graph = list(map(int, input().split()))
data_graph = [1, 2, 3, 11, 23, -1, 2]


class Data:
    def __init__(self, data: list, is_shown=True):
        self.data = data
        self.is_shown = is_shown

    def set_data(self, data):
        self.data = data

    def show_table(self):
        print(*self.data) if self.is_shown else print('No')

    def show_graph(self):
        print('график. показать') if self.is_shown else print('No')

    def show_bar(self):
        print('bar') if self.is_shown else print('No')

    def set_show(self, fl_show: bool):
        self.is_shown = fl_show


dt = Data(data_graph)
dt.show_table()
dt.show_graph()
dt.show_bar()
dt.set_show(False)
dt.show_table()
dt.show_graph()
dt.show_bar()
