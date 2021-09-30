from statistics import mean

n = int(input())



def create_matrix(n):
    count = 0
    m = []
    for _ in range(n):
        m = list(map(int, input().split()))
        for i in m:
            if i > mean(m):
                count += 1
        print(count)
        count = 0
        m.clear()
    return


create_matrix(n)

"""
The trace of the matrix
sum = 0
temp = 0
for i in range(n):
    temp = matrix[i][i]
    sum += temp
print(sum)
"""
