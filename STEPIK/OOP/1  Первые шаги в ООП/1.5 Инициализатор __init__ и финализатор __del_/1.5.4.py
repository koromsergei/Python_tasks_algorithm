import random


class Line:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.sp = (a, b)
        self.ep = (c, d)


class Rect:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.sp = (a, b)
        self.ep = (c, d)


class Ellipse:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
lst_class = ["Line", "Rect", "Ellipse"]
for _ in range(20):
    i = random.randint(0, 2)
    a = random.randint(0, 10000)
    b = random.randint(0, 10000)
    c = random.randint(0, 10000)
    d = random.randint(0, 10000)
    if lst_class[i] == "Line":
        elements.append(Line(a, b, c, d))
    elif lst_class[i] == "Rect":
        elements.append(Rect(a, b, c, d))
    elif lst_class[i] == "Ellipse":
        elements.append(Ellipse(a, b, c, d))

for i, value in enumerate(elements):
    if isinstance(value, Line):
        elements[i].sp = (0, 0)
        elements[i].ep = (0, 0)
