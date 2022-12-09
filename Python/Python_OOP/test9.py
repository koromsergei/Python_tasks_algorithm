n = int(input())
n_pow = 6
lst = []

while n_pow >= 0:
    if 2**n_pow <= n:
        n -= 2**n_pow
        lst.append(2**n_pow)
    else:
        n_pow -= 1
print(*lst)