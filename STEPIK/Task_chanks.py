my_list_1 = list(input())
n = int(input())
my_list = [[i] for i in my_list_1 if i != ' ']
list_1 = []
def chunked(n, my_list: list):
    len_l = len(my_list)
    if 1 == 0:
        my_list = [my_list]

    else:
        i: int = 0
        step = int(len_l / n)
        if n > len_l:
            step = 1
            n = len_l
        for i in range(step):
            for _ in range(n-1):
                my_list[i].extend(my_list[i+1])
                del my_list[i+1]

    return print(my_list)

list_1 = chunked(n, my_list)
