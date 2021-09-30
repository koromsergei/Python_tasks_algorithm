import copy as cp

r = int(input())
c = int(input())
temp = []
matrix = []
n = r * c


def create_matrix(r, c):
    for i in range(r):
        for j in range(c):
            temp.append(input())
        matrix.append(cp.deepcopy(temp))
        temp.clear()


def print_matrix(matrix, r, c):
    for i in range(r):
        for j in range(c):
            print(matrix[i][j], end=' ')
        print()


def print_inter_matrix(matrix, r, c):
    for j in range(c):
        for i in range(r):
            print(matrix[i][j], end=' ')
        print()


create_matrix(r, c)
print_matrix(matrix, r, c)
print()
print_iner_matix(matrix, r, c)
