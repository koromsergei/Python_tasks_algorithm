k=list()
while True:
    inp = input()
    if not inp: break
    k.append(inp)
n=len(k)
v=list(map(int,k))
c=0
d=0
z=0
for i in range(n):
    c=v[i]
    for j in range(n):
        d=v[j]
        e=c*d
        for k in range(n):
            p=v[k]
            if k!=i and p==e:
                z+=1
            
            
if z!=0:
    print('ДА')
else:
    print('НЕТ')