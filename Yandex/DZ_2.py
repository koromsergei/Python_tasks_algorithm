N, i, j = map(int, input().split())
between = j - i - 1
beyond = N - between + 2
if beyond > between:
    print(between)
elif between == beyond:
    print(beyond)
else:
    print(beyond)