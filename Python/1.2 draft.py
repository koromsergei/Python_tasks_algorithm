e=int(input(""))
k=list()
for i in range(e):
    k.append(list(input("")))
i1=0
i2=0
i3=0
i4=0                
n=0
#print(k[1])
for j in range (e):
    m=k[j]    
    if len(m)==4:
        if m[0]=="-":
            n1=-1*int(m[1])
            n2=int(m[3])
        if m[2]=="-":
            n2=-1*int(m[3])
            n1=int(m[0])
    
    elif len(m)==5:
        n1=-1*int(m[1])
        n2=-1*int(m[4])
    else:
        n1=int(m[0])
        n2=int(m[2])

    if n1>0 and n2>0:
        i1+=1
    
    if n1<0 and n2>0:
        i2+=1
    if n1<0 and n2<0:
        i3+=1
    if n1>0 and n2<0:
        i4+=1
        
print("Первая четверть:", i1)
print("Вторая четверть:", i2)
print("Третья четверть:", i3)
print("Четвертая четверть:", i4)