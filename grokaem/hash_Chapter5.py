dict = {}
i = 0
while True:
    name = input("Введи имя")
    if dict.get(name) == None:
        dict[name] = i
        i += 1
    else:
        print("ТЫ уже проголосовал!")