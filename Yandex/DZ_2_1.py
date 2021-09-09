N, i, j = map(int, input().split())
stations = list(range(1, N+1)) * 2
print(stations)
if i > j:
    i, j = j, i
between = j - i - 1
count: int = 0
temp_val: int = 0
q: int = j
while temp_val != i:
    count += 1
    temp_val = stations[q]
    q += 1
count = count - 1

print(min(count, between))
