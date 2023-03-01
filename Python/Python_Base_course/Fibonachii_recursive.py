# N = int(input())


def fib_rec(N, f=[]):
    if N < 3:
        return [1, 1]
    else:
        f = fib_rec(N - 1, f)
        f.append(f[len(f) - 1] + f[len(f) - 2])
        return f


print(*fib_rec(7))
