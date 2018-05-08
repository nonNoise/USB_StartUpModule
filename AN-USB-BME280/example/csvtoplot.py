#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
from mpl_toolkits.axes_grid.parasite_axes import SubplotHost
matplotlib.use('Agg')
import pylab

import pandas as pd
import matplotlib.pyplot as plt

import csv
import sys
import time
import pandas as pd

df = pd.read_csv('test.csv',names=('Day', 'Time', 'UnixTime', 'Temp', 'Temp2', 'Hum', 'Hum2', 'Plass', 'Plass2'))
print(df)
print (df["Time"])
Time_ret = df["Time"]
Temp_ret = df["Temp2"]
Hum_ret = df["Hum2"]


_len = len(Time_ret)
_range = range(0, _len)

fig = matplotlib.pyplot.figure(1)
host = SubplotHost(fig, 111)
par1 = host.twinx()
par2 = host.twinx()
par1.axis["right"].set_visible(True)

offset = 60, 0
new_axisline = par2.get_grid_helper().new_fixed_axis
par2.axis["right2"] = new_axisline(loc="right", axes=par2, offset=offset)
par2.axis["right2"].label.set_visible(True)
par2.axis["right2"].set_label("dead")

fig.add_axes(host)
matplotlib.pyplot.subplots_adjust(right=0.75)

host.set_xlim(0, _len)
host.set_ylim(0, 40000)
host.set_xlabel("times")
host.set_ylabel("damage")
par1.set_ylabel("kill")

p1, = host.plot(_range, Time_ret, label="damage")
p2, = par1.plot(_range, Temp_ret, label="kill")
p3, = par1.plot(_range, Hum_ret, label="dead")

par1.set_ylim(0, 20)
par2.set_ylim(0, 20)

host.legend()
host.axis["left"].label.set_color(p1.get_color())
par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right2"].label.set_color(p3.get_color())

matplotlib.pyplot.draw()
matplotlib.pyplot.savefig('test.png')
