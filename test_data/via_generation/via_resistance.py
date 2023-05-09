# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:40:48 2022

@author: casmi
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "Times New Roman"
mpl.rcParams.update({'font.size': 12})

processes = [1, 2, 3, 4]
prebuff = [0, 55.84, 260.94, 108.53]
postbuff = [0, 61.1, 536.66, 90.79]

# hatching = ['/', 'None', 'None', 'None']
# colors1 = ['lightgrey', 'blue', 'blue', 'blue']
# colors2 = ['lightgrey', 'orange', 'orange', 'orange']

x = np.arange(len(processes))
width = 0.35

fig, ax = plt.subplots();
bar1 = ax.bar(x -width/2, prebuff, width, label="before buffing", edgecolor='black')
bar2 = ax.bar(x+width/2, postbuff, width, label="after buffing", edgecolor='black')

#bar1 = ax.bar(x -width/2, prebuff, width, label="Before buffing", color = colors1, edgecolor = 'black')
#bar2 = ax.bar(x+width/2, postbuff, width, label="After buffing", color = colors2, edgecolor ='black')

ax.set_xticks(x)
ax.set_xticklabels(processes)
plt.ylabel("resistance (mΩ)")
plt.xlabel("process")
ax.legend()
plt.tight_layout()

plt.show()
fig.savefig('via_resistance.png', dpi=500)