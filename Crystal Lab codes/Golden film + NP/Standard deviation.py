from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import flask

DATA = pd.read_excel("SD_.xlsx", dtype={'Mean_outf': float, 'SD_f': float, 'L_f': float,
                                       'Mean_outfb': float, 'SD_b': float, 'L_b': float})


mean_f = DATA["Mean_outf"]
stand_dev_f = DATA["SD_f"]
laser_f = DATA["L_f"]

mean_b = DATA["Mean_outfb"]
stand_dev_b = DATA["SD_b"]
laser_b = DATA["L_b"]

# Plot the sinus function
plt.plot(laser_f, mean_f, ".", color="black", label="forward")
plt.plot(laser_b, mean_b, ".", color="red", label="backward")

# Plot the confidence interval
plt.fill_between(laser_f, (mean_f - stand_dev_f), (mean_f + stand_dev_f), color='black', alpha=0.3)
plt.fill_between(laser_b, (mean_b - stand_dev_b), (mean_b + stand_dev_b), color='red', alpha=0.4)

location = ['upper left']
plt.legend(loc=location[0])
plt.xlabel("P_in (mW)")
plt.ylabel("P_out (mW)")

plt.show()