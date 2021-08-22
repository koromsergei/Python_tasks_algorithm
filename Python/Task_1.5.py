"""
x=list(map(int,input().split()))
k=0
for i in range(len(x)-1):
    if x[i+1]>x[i]:
        k+=1
print(k+1)

"""




