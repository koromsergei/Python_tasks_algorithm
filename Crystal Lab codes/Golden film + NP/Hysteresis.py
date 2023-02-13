from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

DATA = pd.read_excel("data.xlsx", dtype={'Inf1': float, 'Outf1': float, 'Inb1': float, 'Outb1': float,
                                        'Inf2': float, 'Outf2': float, 'Inb2': float, 'Outb2': float,
                                        'Inf4': float, 'Outf4': float, 'Inb4': float, 'Outb4': float,
                                        'Inf5': float, 'Outf5': float, 'Inb5': float, 'Outb5': float,
                                        'Inf6': float, 'Outf6': float, 'Inb6': float, 'Outb6': float,
                                        'Inf7': float, 'Outf7': float, 'Inb7': float, 'Outb7': float,
                                        'Inf8': float, 'Outf8': float, 'Inb8': float, 'Outb8': float,
                                        'Inf9': float, 'Outf9': float, 'Inb9': float, 'Outb9': float,
                                        'Inf10': float, 'Outf10': float, 'Inb10': float, 'Outb10': float})


for i in range(1, 10):
    if i == 3:
        continue
    inf = DATA[f"Inf{str(i)}"]
    inb = DATA[f"Inb{str(i)}"]
    outf = DATA[f"Outf{str(i)}"]
    outb = DATA[f"Outb{str(i)}"]
    plt.plot(inf, outf, ".", color="black", label="forward")
    plt.plot(inb, outb, ".", color="red", label="backward")

    location = ['upper left']
    plt.legend(loc=location[0])
    plt.xlabel("P_in (mW)")
    plt.ylabel("P_out (mW)")

    plt.show()
