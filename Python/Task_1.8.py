t=input()
r=input()
k='камень'
n='ножницы'
b='бумага'
s='Спок'
y='ящерица'

if t==r:
    print('ничья')

elif r==k and t==n or r==b and t==k or r==n and t==b or r==k and t==y or r==y and t==s or r==s and t==n or r==n and t==y or r==y and t==b or r==b and t==s or r==s and t==k:
    print('Руслан')
else:
    print('Тимур')
