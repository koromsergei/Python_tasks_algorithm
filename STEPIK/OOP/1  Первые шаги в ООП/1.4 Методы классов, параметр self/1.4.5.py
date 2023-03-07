class Graph:
    LIMIT_Y = [0, 10]

    def __init__(self):
        self.data = None

    def set_data(self, data: list):
        self.data = data

    def draw(self):
        print(*[i for i in self.data if i in range(self.LIMIT_Y[0], self.LIMIT_Y[1] + 1, 1)])


a = Graph()
a.set_data([1, 2, 3, 43, 5, 6, 7, 8, 9, 12, 21, 11])
