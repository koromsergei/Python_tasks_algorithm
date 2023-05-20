class WordString:
    def __init__(self, name = ''):
        self.name = name

    def __len__(self):
        return len(self.name)

    def __call__(self, *args, **kwargs):
        indx = args[0]
        return self.name.split()[indx]


w1 = WordString('Hello World любимый')
print(len(w1))
print(w1(1))