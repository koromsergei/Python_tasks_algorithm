x, y, z = map(int, input().split())
if x <= 12 and y > 12:
    print(1)
elif y <= 12 and x > 12:
    print(1)
elif y == x:
    print(1)
elif x < 12 and y < 12:
    print(0)
else:
    print(0)