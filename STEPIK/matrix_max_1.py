n = int(input())


def create_matrix(n):
    """
    this function makes a matrix from input
    :param n:
    :return:
    """
    m = []
    for _ in range(n):
        m.append(list(map(int, input().split())))
    return m


def max_2_3(m):
    """
    this function finds max value at the 2d and 3rd parts
    :param m:
    :return:
    """
    temp = []
    for i in range(n):
        for j in range(0, i+1, 1):
            temp.append(m[i][j])
    max_m = max(temp)
    return max_m


def max_2_4(m):
    """
    this function finds max value at the 2d and 4th parts
    :param m:
    :return:
    """
    temp = []
    for i in range(n):
        for j in range(n):
            if i >= j and i <= n - j - 1:
                temp.append(m[i][j])
            elif i <= j and i >= n - j - 1:
                temp.append(m[i][j])
    max_m = max(temp)
    return max_m


def matrix_sum(m):
    """
    this function counts sum of all quaters
    :param m:
    :return:
    """
    quater_1 = []
    quater_2 = []
    quater_3 = []
    quater_4 = []
    for i in range(n):
        for j in range(n):
            if i > j and i < n - j - 1:
                quater_2.append(m[i][j])
            elif i < j and i > n - j - 1:
                quater_4.append(m[i][j])
            elif i > j and i > n - j - 1:
                quater_3.append(m[i][j])
            elif i < j and i < n - j - 1:
                quater_1.append(m[i][j])
    print('Верхняя четверть:', sum(quater_1))
    print('Правая четверть:', sum(quater_4))
    print('Нижняя четверть:', sum(quater_3))
    print('Левая четверть:', sum(quater_2))
    return


matrix = create_matrix(n)
#max = max_under_main_diag(matrix)
#max = max_2_4(matrix)
#print(max)
matrix_sum(matrix)