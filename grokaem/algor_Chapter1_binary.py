import numpy as np
import math

a = int(input("Введите число: "))
#a = 77
sorted_list = [i for i in range(1, 101)]
m = len(sorted_list)
mid = int(m / 2)


def index_search(sorted_list):
    """
    This function searches the index of "a" in sorted list by binary method
    """
    return sorted_list.index(a)


print(math.log2(1000000000))

def index_binary_search(sorted_list):
    n = len(sorted_list)
    while n != 1:
        n = len(sorted_list)
        mid = int(n / 2)
        if a > sorted_list[mid-1]:
            sorted_list = sorted_list[mid:]
        elif a < sorted_list[mid-1]:
            sorted_list = sorted_list[0:mid-1]
        elif a == sorted_list[mid-1]:
            index = a
            break
    return None
    print(sorted_list[mid-1] - 1)

index_binary_search(sorted_list)