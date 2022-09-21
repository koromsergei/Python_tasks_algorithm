list1 = [1, 2, 3, 4]
print(list1)
n = 0
i = 1

"""
recursive function
"""
def sum(list1, i):
    if len(list1) == 1:
        return
    list1 = sum(list1[i:], i + 1)
    print(list1)
    i += 1
    #sum(list1, i)

    return

sum(list1, i)