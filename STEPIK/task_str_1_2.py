my_list = list(input())
my_list_1 = []
for i in my_list:
    if i != ' ':
        my_list_1.append([i])
i = 0
len_l = len(my_list_1)
while i != len_l - 1:
    if my_list_1[i+1] == my_list_1[i] or my_list_1[i+1][0] == my_list_1[i][0]:
        my_list_1[i].extend(my_list_1[i+1])
        del my_list_1[i+1]
        i = 0
    else:
        i += 1
    len_l = len(my_list_1)
print(my_list_1)
