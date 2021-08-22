a=list(map(int,input().split()))
b=list()
c=0
i=0
l=len(a)-1
b.append(a[l])
for i in range(l):
    
    b.append(a[i])


v=str(b).strip('[]')
print(v.replace(",",""))