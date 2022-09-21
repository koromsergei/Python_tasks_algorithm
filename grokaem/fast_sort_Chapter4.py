def qsort(list_main):
    if len(list_main) > 1:
        list1 = []
        list2 = []
        i = int(len(list_main) / 2)
        for j in list_main:
            if j < list_main[i]:
                list1.append(j)
            if j > list_main[i]:
                list2.append(j)
        return qsort(list1) + list_main[i:i+1] + qsort(list2)
    else:
        return list_main
    #list1.append(list_main[i])
    print(list1 + list2)
list_main = [2, 1, 6, 3, 5, 8, 4, 7, 9]
print(qsort(list_main))