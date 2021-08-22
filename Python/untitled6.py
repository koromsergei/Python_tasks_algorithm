n=int(input(""))
k=int(input(""))
L1=list(range(1, n+1))
L=list()
L = k*list(range(1, n+1))+L1
K=k-1
print (L)

for i in range(k,len(L), k):
    print(i-1)
    print (L[i-1])