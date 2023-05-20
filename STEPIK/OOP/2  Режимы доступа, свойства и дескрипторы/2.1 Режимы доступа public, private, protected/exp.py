from string import digits, ascii_letters
import random
name = 'sadasdgmailcom'
test = ascii_letters + digits + '@' + '.'
a = set(name)
print(a)
print(set(test))
print(set(a).issubset(test))
