lst_in = ['3 Сергей', '5 Николай', '4 Елена', '7 Владимир', '5 Юлия', '4 Светлана']
lst_in_num = [int(i.split()[0]) for i in lst_in]
lst_in_nam = [i.split()[1] for i in lst_in]

dates_dict = dict.fromkeys(lst_in_num)
lst_in = [i.split() for i in lst_in]
test_d = {}
for i in lst_in:
    if i[0] not in test_d.keys():
        test_d[int(i[0])] = i[1]
    else:
        break

print(test_d)
