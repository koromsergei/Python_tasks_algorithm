a=input("")
c=list(a)
d=list()
if len(c)==5:
    for i in range (len(c)):
        d.append(c[len(c)-1-i])
    print(int(''.join(map(str, d))))
elif len(c)==6:
    d.append(c[0])
    for i in range (1,len(c),1):
        d.append(c[len(c)-i])    
    print(int(''.join(map(str, d))))
