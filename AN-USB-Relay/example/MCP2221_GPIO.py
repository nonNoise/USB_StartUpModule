from PyMCP2221A import PyMCP2221A

import time

print('-'*20)
print('MCP2221(A) GPIO Test')
print('-'*20)
gpio = PyMCP2221A.PyMCP2221A(devnum=1)
gpio.GPIO_Init()
gpio.GPIO_0_OutputMode()
print(" CTRL+C keys to exit.")
while 1:
    gpio.GPIO_0_Output(1)
    time.sleep(0.2)
    gpio.GPIO_0_Output(0)
    time.sleep(0.8)

    gpio.GPIO_1_Output(1)
    time.sleep(0.2)
    gpio.GPIO_1_Output(0)
    time.sleep(0.2)
    


