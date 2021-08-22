m=int(input(""))
k=list()
i1=0
i2=0
i3=0
i4=0
for i in range(m):
    x,y=map(int,input().split())

    if x>0 and y>0:
        i1+=1
    
    if x<0 and y>0:
        i2+=1
    if x<0 and y<0:
        i3+=1
    if x>0 and y<0:
        i4+=1
                      
print("Первая четверть:", i1)
print("Вторая четверть:", i2)
print("Третья четверть:", i3)
print("Четвертая четверть:", i4)