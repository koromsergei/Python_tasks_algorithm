import copy as cp

my_list_1 = list(input())
my_list = [i for i in my_list_1 if i != ' ']
my_list_2 = []
my_list_2.append([' '])
temp_list = []
"""
for i in my_list:
    my_list_2.append(i)
"""
i: int = 0
k: int = 0
j: int = 0
len_ = len(my_list)
lim = len_ - k
while k != len_:
    while i != lim:
        j = i + k + 1
        my_list_2.append(cp.deepcopy(my_list[i:j]))
        i += 1
    k += 1
    lim = len_ - k
    i = j = 0

print(my_list_2)