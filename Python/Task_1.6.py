n=int(input())
k=list()
for i in range(n):
    k.append(input())

p=int(input())
v=list(map(int,k))
c=0
d=0
z=0
for i in range(n):
    c=v[i]
    for j in range(n):
        d=v[j]
        e=c*d
        if j!=i:
            for k in range(n):
                if k!=i and p==e:
                    z+=1
        e=0
            
if z!=0:
    print('ДА')
else:
    print('НЕТ')