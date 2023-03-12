lst_in = ['Номер;Имя;Оценка;Зачет',
          '1;Портос;5;Да',
          '2;Арамис;3;Да',
          '3;Атос;4;Да',
          "4;д'Артаньян;2;Нет",
          '5;Балакирев;1;Нет']


sort_dict = {'Имя': '0', 'Зачет': '1', 'Оценка': '2', 'Номер': '3'}
sort_lst = [1, 3, 2, 0]
lst_ = [i.split(";") for i in lst_in]

print(lst_)
d = []
for i in lst_:
    if i != lst_[0]:
        i[0] = int(i[0])
        i[2] = int(i[2])
    d.append(sorted(i, key=lambda x: sort_lst.index(i.index(x))))

d[1:].sort(key=lambda x: x[2])
d = [tuple(i) for i in d]
t_sorted = tuple(d)
print(t_sorted)



