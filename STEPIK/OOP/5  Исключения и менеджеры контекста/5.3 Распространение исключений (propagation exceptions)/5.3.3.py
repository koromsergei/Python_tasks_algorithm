def input_int():
    a = input().split()
    try:
        c = [int(i) for i in a]
        return tuple(c)
    except ValueError as e:
        print(e)
        return input_int()


print(input_int())

# def input_int_num():
#     a = input().split()
#     a = [int(i) for i in a]
#     return a
# try:
#     print(input_int_num())
# except ValueError as e:
#     print(e)
#     print(input_int_num())
#