# lst = input().split()
lst = ["+71234567890", "+71234567854", "+61234576890", "+52134567890", "+21235777890", "+21234567110", "+71232267890"]
temp_index = []
for i in lst:
    temp_index.append(i[0:2])
index = []
[index.append(i) for i in temp_index if i not in index]
d = dict.fromkeys(index)


lst_ = []
for j in d:
    for i in lst:
        if i[0:2] == j:
            lst_.append(i)
    d[j] = lst_
    lst_ = []

print(*sorted(d.items()))