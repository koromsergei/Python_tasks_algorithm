def simple_num():
    num = 3
    while True:
        for i in range(2, num, 1):
            if num % i == 0:
                num += 1
                break
        else:
            yield num
            num += 1



it = simple_num()
for i in range(20):
    print(next(it), end=" ")
