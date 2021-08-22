n=int(input(""))
k=int(input(""))
L = list(range(1, n+1))
K=k-1
while len(L)!=k:
    
    L.pop(K)
    L=L[K:]+L[:K]
   
r=0
i=0
j=0
q=len(L)
f=list()
L1=list()
LL=list()
if n!=2:
    L.pop(K)
print(L)
L1=L
for t in range(k): 
    
    while len(L)!=k:
        f.append(L1[r])
        L=L+f# добавили i первых элементов в конец 
        r+=1
        f.clear()
    print(L)
    q=len(L)
    if len (L)==2 and L[0]==L[1]:
        break    
    for j in range(q):    
        if L[j]!=L[len(L)-1] or j==len(L)-1:
            LL.append(L[j])#добавили элемент, совпадающий с последним
        
    L=LL.copy()
    LL.clear()

    if len (L)==2 and L[0]==L[1]:
        break       
    print(L)
    L1.clear()
    #L1=k*L[:len(L)-r]
    #print("L1=", L1 )
    L=L[:len(L)-r]
    L1=k*L
    print("L1=", L1 )
    if len (L)==2 and L[0]==L[1]:
        break    
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