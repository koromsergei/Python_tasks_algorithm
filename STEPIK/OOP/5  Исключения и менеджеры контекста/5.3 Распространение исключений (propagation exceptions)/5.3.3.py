def input_int():
    a = input().split()
    try:
        print(a)
        return [int(i) for i in a]
    except ValueError as e:
        print(e)
        input_int()


print(input_int())
