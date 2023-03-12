# lst = list(map(int, input().split()))
lst1 = [1, 2, 8, 4, 5, 6, 7, 3]
# lst1 = [3, 2, 1, 4]
lst2 = [1, 2, 5, 7]


def split_list(lst: list):
    n = int(len(lst) / 2)
    lst_1 = lst[:n]
    lst_2 = lst[n:]
    if len(lst_1) > 1:
        lst_1 = split_list(lst_1)
    if len(lst_2) > 1:
        lst_2 = split_list(lst_2)
    return split_sorted(lst_1, lst_2)


def split_sorted(lst_1: list, lst_2: list, lst_res=None) -> list:
    if lst_res is None:
        lst_res = []
    if len(lst_1) == 0:
        lst_res += lst_2
        return lst_res
    elif len(lst_2) == 0:
        lst_res += lst_1
        return lst_res
    else:
        if lst_1[0] <= lst_2[0]:
            lst_res.append(lst_1.pop(0))
            return split_sorted(lst_1, lst_2, lst_res)
        elif lst_2[0] < lst_1[0]:
            lst_res.append(lst_2.pop(0))
            return split_sorted(lst_1, lst_2, lst_res)



print(split_list(lst1))
# print(split_sorted(lst1, lst2))
