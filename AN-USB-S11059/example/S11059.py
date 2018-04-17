# -*- encoding:utf8 -*-
import AKI_I2C_S11059
#akilibのAAKI_I2C_S11059を使用する事を宣言
import time
#timeライブラリ

S11059 = AKI_I2C_S11059.AKI_I2C_S11059()
#S11059をI2C_1で使用する事を宣言
S11059.Init()
#S11059特有の初期化処理を行います。

print ("RED = 0x%02X" % S11059.RED())
#赤色9の光の強さを測定します
print ("GREEN = 0x%02X" % S11059.GREEN())
#緑色の光の強さを測定します
print ("BLUE = 0x%02X" % S11059.BLUE())
#青色の光の強さを測定します
print ("IR = 0x%02X" % S11059.IR())
#赤外線の光の強さを測定します

from xtermcolor import colorize
while 1:



    print ("R:0x%02X G:0x%02X B:0x%02X IR:0x%02X " % S11059.RGBISens())
    
    if(S11059.RED()>S11059.GREEN() and  S11059.RED()>S11059.BLUE()):
        print(colorize("■",rgb=0xFF0000))
    if(S11059.GREEN()>S11059.RED() and  S11059.GREEN()>S11059.BLUE()):
        print(colorize("■",rgb=0x00FF00))
    if(S11059.BLUE()>S11059.GREEN() and  S11059.BLUE()>S11059.RED()):
        print(colorize("■",rgb=0x0000FF))
    #RGB＋IRの光の強さを測定します
    time.sleep(0.8)
