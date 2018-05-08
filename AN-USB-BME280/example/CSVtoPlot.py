
datefile = "2018_05_06"

import pandas as pd
df = pd.read_csv( datefile+'.csv', names=('Date', 'Time', 'UnixTime','Temp','Temp2','Humi','Humi2','Press','Press2') )

import numpy as np
import matplotlib.pyplot as plt

#日本語化
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='./font/ipam.ttf', size=14)

#dateフォーマット変換
import matplotlib.dates as mdates
from datetime import datetime 
Time = []
for i in df['Time']:
    Time.append(datetime.strptime(i, '%H:%M:%S'))


print(type(df['Time'][0]))
print(type(Time[0]))
print(df["Date"][0])

plt.figure(figsize=(10,10))

ax1 = plt.subplot(3,1,1)

plt.grid(color='gray')
#時間表示用
xfmt = mdates.DateFormatter("%H:%M")
ax1.xaxis.set_major_formatter(xfmt)
ax1.set_xlim(datetime.strptime('00:00:00', '%H:%M:%S'), datetime.strptime('23:59:00', '%H:%M:%S'))
#ax1.set_ylim(20.00,30.00)
ax1.plot(Time,df['Temp2'],color='r')
plt.title(df["Date"][0]+" 室温 [℃]",fontproperties=font)
#plt.xlabel("X-axis")
plt.ylabel("Y-axis")


ax2 = plt.subplot(3,1,2)
plt.grid(color='gray')
#時間表示用
xfmt = mdates.DateFormatter("%H:%M")
ax2.xaxis.set_major_formatter(xfmt)
ax2.set_xlim(datetime.strptime('00:00:00', '%H:%M:%S'), datetime.strptime('23:59:00', '%H:%M:%S'))
ax2.plot(Time,df['Humi2'],color='b')
plt.title(df["Date"][0]+" 湿度 [%]",fontproperties=font)
#plt.xlabel("X-axis")
plt.ylabel("Y-axis")

ax3 = plt.subplot(3,1,3)
#時間表示用
xfmt = mdates.DateFormatter("%H:%M")
ax3.xaxis.set_major_formatter(xfmt)
ax3.set_xlim(datetime.strptime('00:00:00', '%H:%M:%S'), datetime.strptime('23:59:30', '%H:%M:%S'))
plt.grid(color='gray')
ax3.plot(Time,df['Press2'],color='g')
plt.title(df["Date"][0]+" 気圧 [hPa]",fontproperties=font)
#plt.xlabel("X-axis")
plt.ylabel("Y-axis")


plt.tight_layout() 
plt.savefig(datefile+'.png')
#plt.show()
