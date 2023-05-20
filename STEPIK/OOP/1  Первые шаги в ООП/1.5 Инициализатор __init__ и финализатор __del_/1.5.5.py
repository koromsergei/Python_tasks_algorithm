import random

# a, b, c = map(int, input().split()) # эту строчку не менять
a = random.randint(-1000, 1000)
b = random.randint(-1000, 1000)
c = random.randint(-1000, 1000)

# здесь создайте экземпляр tr класса TriangleChecker и вызовите метод is_triangle() с выводом информации на экран


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.check_list = [self.a, self.b, self.c]

    def is_triangle(self):
        for i in self.check_list:
            if i <= 0 or type(i) not in (int, float):
                return 1
        if a >= b + c or c >= a + b or b >= a + c:
            return 2
        else:
            return 3


lst = []
tpl = ()
ch_1 = 0
ch_2 = 0
ch_3 = 0
for _ in range(100):
    for i in range(100):
        a = random.randint(-10000, 10000)
        b = random.randint(-10000, 10000)
        c = random.randint(-10000, 10000)
        # tpl = tpl + (TriangleChecker(a, b, c),)
        lst.append(TriangleChecker(a, b, c))
    for i in lst:
        if i.is_triangle() == 1:
            ch_1 += 1
        if i.is_triangle() == 2:
            ch_2 += 1
        if i.is_triangle() == 3:
            ch_3 += 1

    print(ch_1, ch_2, ch_3)
    ch_1 = ch_2 = ch_3 = 0
    tpl = ()
    lst.clear()