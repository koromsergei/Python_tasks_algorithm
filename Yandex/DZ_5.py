d = int(input())
x_a: int = 0
y_a: int = 0
x_b: int = d
y_b: int = 0
x_c: int = 0
y_c: int = d
x, y = map(int, input().split())
dic = {}
coord = [(0, 0), (x_b, y_b), (x_c, y_c)]
j = 1
if (x**2 + y**2)**(1/2) <= d*(2)**(1/2) and x >=0 and y >= 0:
    print(0)
else:
    for i in coord:
        x_point, y_point = i
        delta_x = x - x_point
        delta_y = y - y_point
        dic[j] = (delta_y**2 + delta_x**2)**(1/2)
        j += 1
    print(int(min(dic, key=dic.get)))