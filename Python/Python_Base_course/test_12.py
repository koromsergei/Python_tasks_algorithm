lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
lst_in_num = [int(i.split()[0]) for i in lst_in]
lst_in_nam = [i.split()[1] for i in lst_in]

dates_dict = dict.fromkeys(lst_in_num)

temp = [[] for i in range(len(dates_dict))]
_ = 0
for i in dates_dict:
    for j, val in enumerate(lst_in_num):
        if val == i:
            temp[_].append(lst_in_nam[j])  # ошибка

    dates_dict[i] = temp[_]
    print(i, ": ", ", ".join(dates_dict[i]), sep="")
    print("{i}: {\', \'.join(dates_dict[i])}")

    _ += 1



# lst_in = [i.split() for i in lst_in]
# test_d = {}
# for i in lst_in:
#     if i[0] not in test_d.keys():
#         test_d[int(i[0])] = i[1]
#     else:
#         break
#
# print(test_d)
