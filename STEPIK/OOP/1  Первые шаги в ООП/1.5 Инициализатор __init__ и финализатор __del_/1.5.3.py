class Point:
    def __init__(self, x: int, y: int, color='black'):
        self.x = x
        self.y = y
        self.color = color


points = []
j = 1
for i in range(1000):
    if i == 1:
        points.append(Point(j, j, 'yellow'))
        j += 2
    points.append(Point(j, j))
    j += 2

print(points[124].x)