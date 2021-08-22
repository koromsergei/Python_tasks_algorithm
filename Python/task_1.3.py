a=list(map(int,input().split()))
b=list()
c=0
i=0

while i<len(a)-1:
    c=a[i+1]
    b.append(c)
    b.append(a[i])
    i+=2
if len(a)%2!=0:
    b.append(a[len(a)-1])

v=str(b).strip('[]')

print(v.replace(",",""))