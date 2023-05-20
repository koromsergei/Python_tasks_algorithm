class RenderDigits:
    def __call__(self, *args, **kwargs):
        try:
            print(args)
            return int(args[0])
        except ValueError:
            return None


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def foo(*args, **kwargs):
            return [self.render(i) for i in func()]

        return foo


@InputValues(RenderDigits())
def input_dg():
    return input().split()

print(input_dg())
