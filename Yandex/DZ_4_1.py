import numpy as np
n = int(input())
coord_pupils = list(map(int, input().split()))
x = []
med = []
min_c = min(coord_pupils)
max_c = max(coord_pupils)
dic = {}
line = np.linspace(min_c, max_c, max_c - min_c + 1)
for i in line:
    for j in coord_pupils:
        x.append(abs(j-i))
    dic[i] = sum(x)
    x.clear()
print(int(min(dic, key=dic.get)))

#print(dic.get(i[min(dic.values())]))