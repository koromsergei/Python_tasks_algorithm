n = int(input())
m = int(input())
my_list = []
for _ in range(n):
    my_list.append(list(map(int, input().split())))
"""
This code finds max value and prints indexes
i_: int = 0
max_val = max(my_list[0])
for i in range(n-1):
   if max_val < max(my_list[i+1]):
        max_val = max(my_list[i+1])
        i_ = i + 1

print(i_, my_list[i_].index(max_val))
"""
"""
# this code changes i column  and j column
i, j = map(int, input().split())
#my_list[i], my_list[j] = my_list[j], my_list[i] for rows

for q in range(n):
    my_list[q][i], my_list[q][j] = my_list[q][j], my_list[q][i]
    for l in range(m):
        print(my_list[q][l], end=' ')
    print()
    l = 0
"""
while my_list[i][j] == my_list[j][i]:

