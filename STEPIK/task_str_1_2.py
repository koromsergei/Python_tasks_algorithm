my_list = list(input())
my_list_1 = []
for i in my_list:
    if i != ' ':
        my_list_1.append([i])
i = 0
l_m = len(my_list_1)
while i != (l_m - 1):
    j = i
    while my_list_1[j+1] == my_list_1[j]:
        my_list_1[j].extend(my_list_1[j+1])
        del my_list_1[j + 1]
        i = j
        j += 1
    i += 1
print(my_list_1)