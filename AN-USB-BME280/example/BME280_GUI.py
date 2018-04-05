from tkinter import *
from time import *

def BME280_Read(event):
    from PyMCP2221A import BME280
    device = BME280.BME280()
    device.readData()
    print ("temp : %-6.2f ℃" % (device.temperature) )
    print ("hum : %6.2f ％" % (device.var_h) )
    print ("pressure : %7.2f hPa" % (device.pressure/100))

root = Tk()
root.option_add('*font', ('FixedSys', 20))
root.minsize(100, 100)
root.maxsize(400, 400)
buff = StringVar()
buff.set('')

Label(textvariable = buff).pack()

# 時刻の表示
def show_time():
    from PyMCP2221A import BME280
    device = BME280.BME280()
    device.readData()
    str = ""
    #str = str+'USBサイエンスキット'
    #str = str+'\n\n'
    #str = str+'室内環境センサモジュール'
    #sstr = str+'\n\n'
    str = str+"temp : %-6.2f ℃" % (device.temperature)
    str = str+'\n\n'
    str = str+"hum : %6.2f ％" % (device.var_h)
    str = str+'\n\n'
    str = str+"pressure : %7.2f hPa" % (device.pressure/100)
    str = str+'\n\n'    
    str = str+"Time:"+strftime('%I:%M:%S')
    buff.set(str)
    root.after(100, show_time)

show_time()
root.mainloop()