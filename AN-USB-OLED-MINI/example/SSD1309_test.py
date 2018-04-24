from PyMCP2221A import SMBus
import SSD1309
import time
import datetime
i2cbus = SMBus.SMBus()        # 1 = Raspberry Pi but NOT early REV1 board
oled = SSD1309.ssd1309(i2cbus)   # create oled object, nominating the correct I2C bus, default address

# we are ready to do some output ...
from PIL import Image, ImageDraw,ImageFont
# put border around the screen:
oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
fnt = ImageFont.truetype('ipag.ttf', 15)
# Write two lines of text.
oled.canvas.text((40,15),    'Hello', font=fnt,fill=1)
oled.canvas.text((0,40),    '世界よ、ようこそ！',font=fnt, fill=1)
# now display that canvas out to the hardware
oled.display()

while 1:
    for i in range(5):
        oled.cls()
        d = datetime.datetime.today()
        font = ImageFont.truetype('ipag.ttf', 22)
        oled.canvas.text((1, 5),u'%s月%s日' % (d.month, d.day) , font=font,fill=1)
        oled.canvas.text((1, 25),u'%s時%s分%s秒' % (d.hour, d.minute, d.second,), font=font, fill=1)
        oled.display()
        time.sleep(0.5)

    # put border around the screen:
    oled.canvas.rectangle((0, 0, oled.width-1, oled.height-1), outline=1, fill=0)
    fnt = ImageFont.truetype('ipag.ttf', 15)
    # Write two lines of text.
    oled.canvas.text((40,15),    'Hello', font=fnt,fill=1)
    oled.canvas.text((0,40),    '世界よ、ようこそ！',font=fnt, fill=1)
    # now display that canvas out to the hardware
    oled.display()
    time.sleep(2)
