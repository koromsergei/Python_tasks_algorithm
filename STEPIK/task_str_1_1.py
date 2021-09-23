import copy

my_list = list(input())
my_list_2 = []
my_list_3 = []
my_list_4 = []
for i in my_list:
    if i != ' ':
        my_list_2.append([i])

my_list_3 = copy.deepcopy(my_list_2)

i = 0
while i != len(my_list_3) - 1:
    j = i
    while my_list_2[j] == my_list_2[j+1]:
        my_list_3[i].extend(my_list_2[j])
        del my_list_3[j+1]
        j += 1
    i = j
    j = 0