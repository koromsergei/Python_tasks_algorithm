class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False


class GameField:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.field = []

    def init_field(self):
        for i in range(self.n):
            self.field.append([1 for i in range(self.n)])
