from PyMCP2221A import PyMCP2221A
from time import time, sleep, localtime

def MSBtoLEB(data):
    tmp = 0x00
    tmp = tmp | (data&0x80)>>7
    tmp = tmp | (data&0x40)>>5
    tmp = tmp | (data&0x20)>>3
    tmp = tmp | (data&0x10)>>1
    tmp = tmp | (data&0x08)<<1
    tmp = tmp | (data&0x04)<<3
    tmp = tmp | (data&0x02)<<5
    tmp = tmp | (data&0x01)<<7
    return tmp






mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.Reset()
sleep(1)
mcp2221 = PyMCP2221A.PyMCP2221A()
mcp2221.GPIO_Init()
mcp2221.GPIO_0_Output(1) #SCL
mcp2221.GPIO_1_Output(1) #SCL
sleep(1)




def COMMAND1(com1,com2,data,com3):
   
    #mcp2221.GPIO_1_Output(1) #SDA
    mcp2221.GPIO_0_Output(1) #SCL
    mcp2221.GPIO_1_Output(1) #SDA
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_0_Output(0) #SCL
    for i in range(8):
        mcp2221.GPIO_0_Output(0) #SCL
        mcp2221.GPIO_1_Output((com1>>i)&0x01) #SDA
        mcp2221.GPIO_0_Output(1) #SCL
    # ACK
    mcp2221.GPIO_0_Output(0) #SCL
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_0_Output(1) #SCL

    # Stop 
    mcp2221.GPIO_0_Output(0) #SCL
    mcp2221.GPIO_1_InputMode() #SDA
    mcp2221.GPIO_0_Output(1) #SCL
#------------------------------------------------#
    mcp2221.GPIO_0_Output(1) #SCL
    mcp2221.GPIO_1_Output(1) #SDA
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_0_Output(0) #SCL
    for i in range(8):
        mcp2221.GPIO_0_Output(0) #SCL
        mcp2221.GPIO_1_Output((com2>>i)&0x01) #SDA
        mcp2221.GPIO_0_Output(1) #SCL

    # ACK
    mcp2221.GPIO_0_Output(0) #SCL
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_0_Output(1) #SCL
#------------------------------------------------#
    #print(len(data))
    for p in range(len(data)):
        for i in range(8):
            mcp2221.GPIO_0_Output(0) #SCL
            mcp2221.GPIO_1_Output((data[p]>>i)&0x01) #SDA
            mcp2221.GPIO_0_Output(1) #SCL
        # ACK
        mcp2221.GPIO_0_Output(0) #SCL
        mcp2221.GPIO_1_Output(0) #SDA
        mcp2221.GPIO_0_Output(1) #SCL
    # Stop 
    mcp2221.GPIO_0_Output(0) #SCL
    mcp2221.GPIO_1_InputMode() #SDA
    mcp2221.GPIO_0_Output(1) #SCL
#------------------------------------------------#
    mcp2221.GPIO_0_Output(1) #SCL
    mcp2221.GPIO_1_Output(1) #SDA
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_1_Output(0) #SDA
    mcp2221.GPIO_0_Output(0) #SCL
    for i in range(8):
        mcp2221.GPIO_0_Output(0) #SCL
        mcp2221.GPIO_1_Output((com3>>i)&0x01) #SDA
        mcp2221.GPIO_0_Output(1) #SCL

    # ACK
    #mcp2221.GPIO_0_Output(0) #SCL
    #mcp2221.GPIO_1_Output(0) #SDA
    #mcp2221.GPIO_0_Output(1) #SCL
    # Stop 
    mcp2221.GPIO_0_Output(0) #SCL
    mcp2221.GPIO_1_InputMode() #SDA
    mcp2221.GPIO_0_Output(1) #SCL
    #exit()    
    
seg = [0]*10
seg[0] = 0x3F
seg[1] = 0x06
seg[2] = 0x5B
seg[3] = 0x4F
seg[4] = 0x66
seg[5] = 0x6D
seg[6] = 0x7D
seg[7] = 0x27
seg[8] = 0x7F
seg[9] = 0x6F
num = 0
while 1:
    t = localtime()
    #sleep(1 - time() % 1)
    d0 = t.tm_hour // 10 if t.tm_hour // 10 else 0
    d1 = t.tm_hour % 10
    d2 = t.tm_min // 10
    d3 = t.tm_min % 10
    COMMAND1(0x40,0xC0,[seg[d0],seg[d1],seg[d2],seg[d3],0x00],0x80+0x08+5)
    COMMAND1(0x40,0xC0,[seg[d0],seg[d1],seg[d2],seg[d3],0x03],0x80+0x08+7)

    #COMMAND1(0x40,0xC0,[seg[d0],seg[d1],seg[d2],seg[d3],0x03],0x80+0x08+7)


#COMMAND1(0x00,0xC0,0xFF,0x8F)

