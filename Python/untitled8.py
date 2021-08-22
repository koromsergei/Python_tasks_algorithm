n=int(input(""))
k=int(input(""))
L1=list(range(1, n+1))
L=list()
L = k*list(range(1, n+1))+L1+L1
K=k-1
print (L)
LL=list()
Q=list()
while len(L)!=1:
    h=L[K]
    print(h)
    L=L[k:]
    print(L)
    q=len(L)
    for j in range(q):    
        if L[j]!=h:
            LL.append(L[j])
        
    L=LL.copy()
    Q=LL.copy()
    LL.clear()
    h=0
    q=0
    j=0
    print(L)
    print('__________')

print(L)  
"""    
if k%2==0:
    print(L[1])
else:
    print(L[0])
"""    