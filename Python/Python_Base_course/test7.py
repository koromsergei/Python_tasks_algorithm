lst = list(input())
lst_new = []
sum_neg = 0
sum_pos = 0

for i in lst:
    if i != " ":
        lst_new.append(i)

equa = "".join(lst_new)
pos_equa = equa.replace(' ', '').split("+")

pos_numbers = []
neg_numbers = []

for i in pos_equa:
    if i.isdigit():
        pos_numbers.append(i)
    else:
        neg_numbers.append(i)

sum_pos = sum([int(i) for i in pos_numbers])

for i in neg_numbers:
    temp = i.split("-")
    temp = [i for i in temp if i.isdigit()]
    sum_temp = int(temp[0]) - int(temp[1])
    sum_neg += sum_temp
    temp = 0
    sum_temp = 0

#print(sum_pos)
#print(sum_neg)
print(sum_neg + sum_pos)