
L = list([1,2,3,4,5,6,7,8,9,10,11,12])
i=7

L=L[i:]
LL=list()
L1=list()
q=len(L)
print(L)




"""
for i in range(3):
    for j in range(q):    
        if L[j]!=L[len(L)-1] or j==len(L)-1:
            LL.append(L[j])#добавили элемент, совпадающий с последним
        print(LL)    
        
    L=LL.copy()
    LL.clear()
    q=len(L)
    j=0
    print('____________')
L1=5*L
print(L1)
"""