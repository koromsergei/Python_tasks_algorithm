import math
n = int(input())
list_ = []


def pascal(n):
    for k in range(n+1):
        list_.append(int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))
    return print(list_)

pascal(n)
