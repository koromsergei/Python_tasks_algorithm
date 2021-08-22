n=int(input(""))
k=int(input(""))
L = list(range(1, n+1))
K=k-1
while len(L)>k:
    if n==2 and k==1:
        
        break
    L.pop(K)
    L=L[K:]+L[:K]
    
r=0
i=0
j=0
f=list()
if n!=2:
    L.pop(K)
print(L)
while len(L)!=1:
    if n==2 and k==1:
        break
    
    
    while len(L)!=k:
        f.append(L[r])
        L=L+f# добавили i первых элементов в конец 
        r+=1
        f.clear()
    print(L)
    for q in range (k):
        if L[j]==L[len(L)-1]:
            L.pop(j)#удалили элемент, совпадающий с последним
            j=-1
        j+=1
        if j>len(L)-1:
            break 
    print(L)
    L=L[:len(L)-i-1]
    
    r=0
    q=0
    i+=1
    j=0
    K=k-1
    print(L)
    print('___________')


print(L[0])
"""
if k%2==0 and k!=2 or k==1 :
    print(L[1])
else:
    print(L[0])  
"""