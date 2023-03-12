lst = list(map(int, input().split()))
_ = n = len(lst)
while _ != 2:
    for i in range(n - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    _ -= 1
    n = _
print(*lst)
