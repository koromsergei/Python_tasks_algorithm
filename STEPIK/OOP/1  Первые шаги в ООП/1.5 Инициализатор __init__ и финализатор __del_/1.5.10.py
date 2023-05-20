# можно допилить
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
        self.field_size = self.n * self.n
        self.mines = self.mine_index()
        self.field = []
        self.init_field()

    def init_field(self):
        lst = []
        for i in range(self.field_size):
            lst.append(1) if i not in self.mines else lst.append(0)
        j = 0
        i = 0
        while j != self.n:
            self.field.append(lst[i:i + self.n])
            j += 1
            i += self.n

    def mine_index(self):
        mines = []
        while len(mines) < self.m:
            rand_int = random.randint(0, self.field_size - 1)
            if rand_int not in mines:
                mines.append(rand_int)
        return mines

    def show_field(self):
        for i in self.field:
            print(*i)


g = GameField(10, 50)
# print(len(g.mines), g.mines)
g.show_field()
