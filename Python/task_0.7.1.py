n=int(input(""))
k=int(input(""))
L = list(range(1, n+1))
K=k-1
while len(L)>k:
    L.pop(K)
    L=L[K:]+L[:K]
    
r=0
i=1
j=0
f=list()
L.pop(K)
print(L)
print('Start')
while L[0]!=L[1]:   
    while len(L)!=k:
        f.append(L[r])
        L=L+f# добавили i первых элементов в конец 
        r+=1
        f.clear()
    print(L)      
    while len(L)==k:
        if L[j]==L[K] and j!=K:
            L.pop(j)#удалили элемент, совпадающий с последним 
    

            
          
    L=L[:len(L)-i]      
    i+=1   
    r=0    
    print(L)
    print('___________')    
print(L)
print(L[0])


    
"""
    #while len(L)==k:
    for j in range(len(L)):
        if L[j]==L[K] and j!=K:
            L.pop(j)#удалили элемент, совпадающий с последним 
            K=K-1
            
"""


"""

for i in L:
        if L.count(i) > 1:
            L.remove(i)
"""