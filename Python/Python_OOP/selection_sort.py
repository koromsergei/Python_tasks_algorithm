lst = list(map(int, input().split()))
n = len(lst)
for i in range(n):
    j = i
    while j < n:
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
        j += 1

print(*lst)
