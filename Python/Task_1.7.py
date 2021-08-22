t=input()
r=input()
k='камень'
n='ножницы'
b='бумага'


if t==r:
    print('ничья')

elif r==k and t==n or r==b and t==k or r==n and t==b:
    print('Руслан')
else:
    print('Тимур')

           
