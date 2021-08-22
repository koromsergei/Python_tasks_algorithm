n=int(input(""))
k=int(input(""))
L = list(range(1, n+1))
K=k-1
f=list()
r=0
while len(L)>k:
    L.pop(K)
    L=L[K:]+L[:K]
    while len(L)!=k:
        f.append(L[r])
        L=L+f# добавили i первых элементов в конец 
        r+=1
        f.clear()
    r=0
    
r=0
i=1
j=0
f.clear()
L.pop(K)
print(L)

while len(L)>2:   
    while len(L)!=k:
        f.append(L[r])
        L=L+f# добавили i первых элементов в конец 
        r+=1
        f.clear()
    print(L)
    for j in range (k):
        if L[j]==L[K]:
            L.pop(j)#удалили элемент, совпадающий с последним 
        j+=1
    print(L)
    #L=L[:len(L)-i]
    print(L)
    print('___________')
    r=0
    i+=1
    j=0

if k%2==0 and k!=2 or k==1 :
    print(L[1])
else:
    print(L[0])     