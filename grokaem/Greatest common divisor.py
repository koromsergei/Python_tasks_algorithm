def foo(a, b):
    if a > b:
        a, b = b, a
    while b % a != 0:
        a = b % a
    return a


print(foo(54, 25))
