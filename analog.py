import RPi.GPIO as GPIO
import time
import Adafruit_MCP3008
	
try:

	# Software config 
	CLK = 18
	MISO = 23
	MOSI = 24
	CS = 25
	mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

	print('Reading MCP3008 values, press CTRL-C to quit...')
	print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} |  {6:>4} | {7:>4} |'.format(*range(8)))
	print ('-' * 57)
	
	while True:
		values = [0]*8
		for i in range(8):
			values[i] =  mcp.read_adc(i)
		print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} |  {6:>4} | {7:>4} |'.format(*values))
		time.sleep(0.5)
except KeyboardInterrupt:
	print "You've exited the program"
finally:
	GPIO.cleanup()

