N = int(input())
K = int(input())
possib = []
for i in range(N):
    possib.append(float(input()))
possib_K= []
all_sum = sum(possib)
sum_K = []
k = 0
t = 0
for i in range(N):
    for j in range(K):
        if i + j < N:
            k = possib[i + j]
            t += k
    sum_K.append(all_sum - t)
    t = 0
print(min(sum_K))
