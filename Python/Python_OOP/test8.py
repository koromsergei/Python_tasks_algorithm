# n = int(input())
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")


lst = [[1, 0, 0, 1, 0], [0, 0, 0, 1, 1], [1, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 0, 0, 0, 1]]
lst_rows = [[0]*5 for i in range(4)]
print(lst_rows)

j = 0
k = 0
for j in range(4):
    for k in range(5):
        lst_rows[j][k] = lst[j][k] * lst[j + 1][k]





print(lst_rows)