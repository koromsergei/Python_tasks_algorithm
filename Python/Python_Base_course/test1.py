from typing import List
import numpy as np
import enum
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 3)
y = np.linspace(0, 100, 20)
z = np.linspace(0, 100, 6)
w = np.linspace(0, 100, 9)


def do_line(coords: List[np.array], order: str, current_position: List=None):
    if current_position is None:
        current_position = []
    if len(coords) > 1:
        for coord in coords[0]:
            do_line(coords[1:], order, [*current_position, coord])
    else:
        for coord in coords[0]:
            temp_coord = [*current_position, coord]
            temp_doc = {order[i]: temp_coord[i] for i in range(len(order))}
            print(**temp_doc)


keys = {
        1: x,
        2: y,
        3: z,
        4: w,
        }
keys_str = {
        1: "x",
        2: "y",
        3: "z",
        4: "w",
        }


order = [1, 2, 3, 4]

do_line([keys[i] for i in order], "".join([keys_str[i] for i in order]))
