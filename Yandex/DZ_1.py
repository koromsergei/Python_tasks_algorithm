DATA = open('DZ_1.txt', 'r')
exit_code = int(input())
ineterc = int(input())
checker= int(input())
if ineterc == 0 and exit_code != 0:
    print (3)
elif ineterc == 0 and exit_code == 0:
    print(checker)
elif ineterc == 1:
    print(checker)
elif ineterc == 4 and exit_code != 0:
    print(3)
elif ineterc == 4 and exit_code == 0:
    print(4)
elif ineterc == 6:
    print(0)
elif ineterc == 7:
    print(1)
else:
    print(ineterc)