class A:
    b = 1

    def __init__(self):
        self.buffer = []

    def get_data(self):
        yield self.buffer
        self.buffer.clear()


A.b = 12
a = A()
a.buffer = [1, 2, 3]
a.get_data()
a.get_data()

print(a.buffer)