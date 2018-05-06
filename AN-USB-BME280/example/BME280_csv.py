#from smbus2 import SMBus
from PyMCP2221A import BME280
import time
device = BME280.BME280()
import csv
from datetime import datetime
step = 60
t = [0]*step
p = [0]*step
h = [0]*step
cnt = 0
while 1:
    
    #------------------------------------------------------#
    # 温度、湿度、気圧のデータを取得
    #------------------------------------------------------#
    device.readData()
    print ("temp : %-6.2f ℃" % (device.temperature) )
    print ("hum : %6.2f ％" % (device.humidity) )
    print ("pressure : %7.2f hPa" % (device.pressure/100))
    
    
    #------------------------------------------------------#
    # 室温の移動平均値計算
    #------------------------------------------------------#
    tmp = 0.0
    for i in range(step):
        tmp = tmp + t[i] 
    temperature = tmp/step
    for i in range(step-1):
        t[i] = t[i+1]
    t[step-1] = device.temperature

    #------------------------------------------------------#
    # 湿度の移動平均値計算
    #------------------------------------------------------#
    tmp = 0.0
    for i in range(step):
        tmp = tmp + h[i] 
    humidity = tmp/step
    for i in range(step-1):
        h[i] = h[i+1]
    h[step-1] = device.humidity

    #------------------------------------------------------#
    # 気圧の移動平均値計算
    #------------------------------------------------------#
    tmp = 0.0
    for i in range(step):
        tmp = tmp + p[i] 
    pressure = tmp/step
    for i in range(step-1):
        p[i] = p[i+1]
    p[step-1] = device.pressure/100

    #------------------------------------------------------#
    # 移動平均値計算の初期値が一周するまでくり変えす
    #------------------------------------------------------#
    if(cnt < step):
        cnt = cnt + 1
    else :
        #------------------------------------------------------#
        # 30秒間隔で計測する
        #------------------------------------------------------#    
        dtime = datetime.now()
        if(dtime.strftime("%S")== "00" or dtime.strftime("%S")== "30" ):
            #------------------------------------------------------#
            # CSVに保存する項目と順序
            #------------------------------------------------------#
            list = [
                    dtime.strftime("%Y/%m/%d"),
                    dtime.strftime("%H:%M:%S"),
                    dtime.strftime('%s'),	#念の為のUnixTime
                    device.temperature,		#センサー値
                    temperature,			#移動平均値
                    device.humidity,		#センサー値
                    humidity,				#移動平均値
                    device.pressure/100,	#センサー値
                    pressure				#移動平均値
                    ]
            print("-"*20)
        
            #------------------------------------------------------#
            # CSVを開き最後の行に追加し、上書き保存する。
            #------------------------------------------------------#
            f = open(dtime.strftime("%Y_%m_%d")+".csv", 'a')
            writer = csv.writer(f, lineterminator='\n')
            writer.writerow(list)
            f.close()
    time.sleep(1)





