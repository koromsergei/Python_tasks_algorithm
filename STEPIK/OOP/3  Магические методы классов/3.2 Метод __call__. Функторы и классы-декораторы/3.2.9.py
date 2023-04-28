class InputDigits:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(args[0])
        return [int(i) for i in self.func(1)]


@InputDigits
def input_dg(a):
    return input().split()


print(input_dg(1233))
