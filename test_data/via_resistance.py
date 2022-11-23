# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:40:48 2022

@author: casmi
"""

import matplotlib.pyplot as plt
import numpy as np

processes = [1, 2, 3, 4]
prebuff = [0, 55.84, 260.94, 108.53]
postbuff = [0, 61.1, 536.66, 90.79]

x = np.arange(len(processes))
width = 0.35

fig, ax = plt.subplots();
bar1 = ax.bar(x -width/2, prebuff, width, label="Before buffing")
bar2 = ax.bar(x+width/2, postbuff, width, label="After buffing")

ax.set_xticks(x)
ax.set_xticklabels(processes)
ax.legend()

plt.show()