# -*- coding: utf-8 -*-
from tkinter import *
from time import *


root = Tk()
root.option_add('*font', ('FixedSys', 20))
root.minsize(200, 100)
root.maxsize(400, 400)
buff = StringVar()
buff.set('')

Label(textvariable = buff).pack()
from PyMCP2221A import BME280
device = BME280.BME280()

def show_time():
    #from PyMCP2221A import BME280
    #device = BME280.BME280()
    device.readData()
    arr = [[0 for i in range(18)] for j in range(20)]

    arr[19] = [29,30,31,32,33,34,35,35,36,37,38,39,40,41,42,43,44]
    arr[18] = [28,29,30,31,32,33,34,35,35,36,37,38,39,40,41,42,43]
    arr[17] = [28,28,29,30,31,32,33,34,35,35,36,37,38,39,40,41,42]
    arr[16] = [27,28,29,29,30,31,32,33,35,35,35,36,37,38,39,40,41]
    arr[15] = [26,27,28,29,29,30,31,32,33,34,34,35,36,37,38,39,39]
    arr[14] = [25,26,27,28,29,29,30,31,32,33,33,34,35,36,37,38,37]
    arr[13] = [25,25,26,27,28,29,29,30,31,32,33,33,34,35,36,37,37]
    arr[12] = [24,25,25,26,27,28,28,29,30,31,32,32,33,34,35,35,36]
    arr[11] = [23,24,25,25,26,27,28,28,29,30,31,31,32,33,34,34,35]
    arr[10] = [22,23,24,24,25,26,27,27,28,29,30,30,31,32,33,33,34]
    arr[9] = [21,22,23,24,24,25,26,27,27,28,29,29,30,31,32,32,33]
    arr[8] = [21,21,22,23,24,24,25,26,26,27,28,29,29,30,31,31,32]
    arr[7] = [20,21,21,22,23,23,24,25,25,26,27,28,28,29,30,30,31]
    arr[6] = [19,20,21,21,22,23,23,24,25,25,26,27,27,28,29,29,30]
    arr[5] = [18,19,20,20,21,22,22,23,24,24,25,26,26,27,28,28,29]
    arr[4] = [18,18,19,20,20,21,22,22,23,23,24,25,25,26,27,27,28]
    arr[3] = [17,18,18,19,19,20,21,21,22,22,23,24,24,25,26,26,27]
    arr[2] = [16,17,17,18,19,19,20,20,21,22,22,23,23,24,25,25,26]
    arr[1] = [15,16,17,17,18,18,19,19,10,21,21,22,22,23,24,24,25]
    arr[0] = [15,15,16,16,17,17,18,19,19,20,20,21,21,22,23,23,24]

    WBGT =  arr[ int(device.temperature-21) ][ int(((device.var_h-20) - (device.var_h-20)%5)/5)  ]

    str = ""
    str = str+"temp : %-6.2f ℃" % (device.temperature)
    str = str+'\n\n'
    str = str+"hum : %6.2f ％" % (device.var_h)
    str = str+'\n\n'
    str = str+"pressure : %7.2f hPa" % (device.pressure/100)
    str = str+'\n\n'    
    str = str+"Time:"+strftime('%I:%M:%S')
    str = str+'\n\n'    
    str = str+"不快指数 : %0.2f " % (device.DI) 
    str = str+'\n\n'    
    if(device.DI > 85):
        str = str+"暑いぃ！"
    elif(device.DI > 80):
        str = str+"汗が出る"
    elif(device.DI > 75):
        str = str+"やや暑い"
    elif(device.DI > 70):
        str = str+"暑くない"	
    elif(device.DI > 65):
        str = str+"快適"
    elif(device.DI > 60):
        str = str+"何も感じない"
    elif(device.DI > 55):
        str = str+"肌寒い"
    else:
        str = str+"寒い"
    str = str+'\n\n'    
    str = str + "暑さ指数: %d" % WBGT
    str = str+'\n\n'    
    if(WBGT > 31):
        str = str+"危険！"
    elif(WBGT > 28):
        str = str+"厳重警戒！"
    elif(WBGT > 25):
        str = str+"警戒"
    elif(WBGT > 21):
        str = str+"注意"
    else:
        str = str+"ほぼ安全"

    buff.set(str)
    root.after(500, show_time)

show_time()
root.mainloop()
