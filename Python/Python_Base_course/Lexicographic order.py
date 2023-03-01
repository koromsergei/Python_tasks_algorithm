def str_min(a, b):
    if len(b) > len(a):
        a, b = b, a
    for i in range(len(b)):
        if b[i] < a[i]:
            return b
        elif b[i] > a[i]:
            return a
    return b


def str_min3(a, *args):
    return str_min(a, str_min(*args))


def str_min4(a, *args):
    return str_min(a, str_min3(*args))

print(str_min("МАТЕМАТИК", "МАТЕМАТИКА"))

print(str_min4('abab', 'aba', 'aab', 'bba'))
