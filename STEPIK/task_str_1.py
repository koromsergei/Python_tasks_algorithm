import copy
from itertools import groupby
str_ = list(input())
list_1 = []
#new_str = [el for el, _ in groupby(str_)]
new_str = []
for x in str_:
    if x not in new_str and x != ' ':
        new_str.append(x)
list_ = [0] * len(new_str)
q: int = 0
for i in new_str:
    for j in str_:
        if j != ' ' and j == i:
            list_1.append(j)
    list_[q] = copy.deepcopy(list_1)
    list_1.clear()
    q += 1
list_ = list(filter(None, list_))
print(list_)