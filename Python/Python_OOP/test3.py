import numpy
import numpy as np

control_keys = {
    0: "x",
    1: "y",
    2: "z",
    3: "w"
}


def control(start, end, step):
    s = int(abs(start - end - 1) / step)
    a = np.linspace(start, end, s)
    print(a)

dic = {"x": [1, 2, 3], "y": [23, 34, 4], "z": [1, 100, 1], "w": [1, 3, 2]}

order = [2, 1, 3, 4]

print(dic.get(control_keys.get(order[0])))
print(control_keys.get(order[0]))

control(*dic.get(control_keys.get(order[0])))


def movement(self, start, end, step):
    arr = int(abs(start - end - 1) / step)
    a = np.linspace(start, end, arr)

    for i in a:
        scanner.goto(x=i)
        self.measurements()


start = 0
end = 100
step = 3



