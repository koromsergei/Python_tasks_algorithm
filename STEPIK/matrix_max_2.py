n = int(input())
m = int(input())


def multi_table(x, y):
    """
    this function returns multiplication table where matrix[i][j] = i * j
    :param x:
    :param y:
    :return matrix:
    """
    matrix = [[0]*y for _ in range(x)]
    for i in range(x):
        for j in range(y):
            matrix[i][j] = i * j
            print(str(matrix[i][j]).ljust(3), end=' ')
        print()

    return matrix


multi_table(n, m)

