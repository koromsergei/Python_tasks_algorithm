c=list(input(""))
d=list()
k=list()
d=c[::-1]
i=3
z=0
while i <len(c): 
    d.insert(i+z,',')
    i+=3
    z+=1
k=d[::-1]
print(''.join(map(str, k)))  
