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
q=len(L)
f=list()
LL=list()
if n!=2:
    L.pop(K)
print(L)
while len(L)!=2:
    if n==2 and k==1:
        break
    if len(L)==1:
        break
    if L[0]==L[1]:
        break    
    
    while len(L)!=k:
        f.append(L[r])
        L=L+f# добавили i первых элементов в конец 
        r+=1
        f.clear()
    print(L)
    q=len(L)
    for j in range(q):    
        if L[j]!=L[len(L)-1] or j==len(L)-1:
            LL.append(L[j])#добавили элемент, совпадающий с последним
        
    L=LL.copy()
    LL.clear()

       
    print(L)
    L=L[:len(L)-r]
    
    r=0
    q=0
    i+=1
    j=0
    K=k-1
    print(L)
    print('___________')
    


if k%2==0 and k!=2 or k==1 :
    print(L[1])
else:
    print(L[0])  
