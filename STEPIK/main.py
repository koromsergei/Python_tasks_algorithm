import math
n = int(input())
list_ = []


def pascal(n):
    for i in range(n):
        for k in range(i+1):
            list_.append(int(math.factorial(i) / (math.factorial(k) * math.factorial(i - k))))
        #list_ = str(list_)
        print(" ".join(str (j) for j in list_))
        list_.clear()
    return 0

pascal(n)
