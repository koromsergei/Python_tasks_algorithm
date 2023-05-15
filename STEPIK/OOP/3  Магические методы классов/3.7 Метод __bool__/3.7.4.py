class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        if self.score > 0:
            return True
        return False


player = [Player('Ivan', 12, 1),
          Player('Lol', 22, 121),
          Player('Kek', 31, -58),
          Player('Sergei', 3, 0),
          Player('Vasya', 11, 1)]

player_filters = list(filter(bool, player))

print([i.name for i in player])
print([i.name for i in player_filters])
