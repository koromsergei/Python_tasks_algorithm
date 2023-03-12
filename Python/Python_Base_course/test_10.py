l = '+71234567890 Сергей\n+71234567810 Сергей\n+51234567890 Михаил\n+72134567890 Николай\n+9898989898 Сергей'
lst = l.split()
name_lst_full = [d for i, d in enumerate(lst) if i % 2 != 0]
phone_lst = [[d] for i, d in enumerate(lst) if i % 2 == 0]

name_lst = []
[name_lst.append(i) for i in name_lst_full if i not in name_lst]
for i, n_value in enumerate(name_lst_full):
    for j, name in enumerate(name_lst_full):
        if i != j and n_value == name:
            phone_lst[i].append(*phone_lst[j])
            phone_lst.pop(j)
            name_lst_full.pop(j)

d = dict.fromkeys(name_lst)
for i, v in enumerate(phone_lst):
    d[name_lst[i]] = v
print(*sorted(d.items()))

