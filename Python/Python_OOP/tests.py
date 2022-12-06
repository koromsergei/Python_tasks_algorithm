# +7(xxx)xxx-xx-xx
check = "+7(xxx)xxx-xx-xx"
lst_chek = list(check)
phone = list(input())

for i in range(len(phone)):
    if i == 1:
        continue
    if 47 < ord(phone[i]) < 58:
        phone[i] = "x"


print(phone[len(phone)])
print("ДА") if phone == lst_chek else print("НЕТ")