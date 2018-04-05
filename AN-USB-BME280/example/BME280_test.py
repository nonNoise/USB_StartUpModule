#from smbus2 import SMBus
from PyMCP2221A import BME280
import time
device = BME280.BME280()
while 1:
	device.readData()
	print ("temp : %-6.2f ℃" % (device.temperature) )
	print ("hum : %6.2f ％" % (device.var_h) )
	print ("pressure : %7.2f hPa" % (device.pressure/100))

	print ("不快指数 : %0.2f " % (device.DI) )
	if(device.DI > 85):
		print("暑いぃ！")
	elif(device.DI > 80):
		print("汗が出る")
	elif(device.DI > 75):
		print("やや暑い")
	elif(device.DI > 70):
		print("暑くない")	
	elif(device.DI > 65):
		print("快適")
	elif(device.DI > 60):
		print("何も感じない")
	elif(device.DI > 55):
		print("肌寒い")
	elif(device.DI > 55):
		print("寒い")

	print("-"*20)
	time.sleep(1)






