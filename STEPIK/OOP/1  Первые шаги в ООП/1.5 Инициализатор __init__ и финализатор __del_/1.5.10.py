import random


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
        self.field_size = self.n * self.n

    def init_field(self):
        lst = []
        j = 0
        for i in range(self.field_size):
            lst.append(1) if i not in self.mine_index() else lst.append(0)
        j = 0
        while j != self.n:
            self.field.append(lst[j:j + 5])
            j += 5

    def mine_index(self):
        mines = []
        for i in range(self.m):
            rand_int = random.randint(0, self.field_size)
            if rand_int not in mines:
                mines.append(rand_int)
        return mines