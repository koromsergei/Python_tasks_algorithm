# n = int(input())
#
# for i in range(2, n):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         print(i, end=" ")


lst_in = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

for i in range(5):
    for j in range(5):
        if lst_in[i][j] != lst_in[j][i]:
            print("НЕТ")
            break
    else:
        continue
    break
else:
    print("ДА")


#
# for i in range(5):
#     print(lst_in[i], end="\n")
#
# print()
# for i in range(5):
#     print(lst_columns[i], end="\n")
# print()
# for i in range(5):
#     print(lst_rows[i], end="\n")


