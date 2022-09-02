# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:08:25 2022

@author: casmi
"""


import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd
import pylab as pl
import numpy as np
plt.rcParams["font.family"] = "Times New Roman"
#mpl.rcParams.update({'font.size': 14})

import IPython as IP
IP.get_ipython().magic('reset -sf')
plt.close('all')

df = pd.read_csv("test2_13_12.csv")

plt.figure(figsize=(6.5,3.5))
plt.plot(df["sample"], df["trace 1"], label="trace 1")
plt.plot(df["sample"], df["trace 2"], label="trace 2")
plt.plot(df["sample"], df["trace 3"], label="trace 3")
plt.plot(df["sample"], df["trace 4"], label="trace 4")
plt.plot(df["sample"], df["trace 5"], label="trace 5")
plt.plot(df["sample"], df["trace 6"], label="trace 6")
plt.plot(df["sample"], df["trace 7"], label="trace 7")
plt.plot(df["sample"], df["trace 8"], label="trace 8")
plt.plot(df["sample"], df["trace 9"], label="trace 9")
plt.plot(df["sample"], df["trace 10"], label="trace 10")
plt.plot(df["sample"], df["trace 11"], label="trace 11")
plt.plot(df["sample"], df["trace 12"], label="trace 12")
#plt.legend(framealpha=1)
plt.xlabel('sample')
plt.ylabel('digital signal')
plt.locator_params(axis="x", nbins=5)
plt.locator_params(axis="y", nbins=2)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig('test2_13_12.png', dpi=500)