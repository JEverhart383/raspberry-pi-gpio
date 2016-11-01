import RPi.GPIO as GPIO, time, os 
	
try:

	DEBUG = 1
	GPIO.setmode(GPIO.BCM)

	def RCtime (RCpin):
        	reading = 0 
        	GPIO.setup(RCpin, GPIO.OUT)
        	GPIO.output(RCpin, GPIO.LOW)
        	time.sleep(0.1)

	        GPIO.setup(RCpin, GPIO.IN)
        	while (GPIO.input(RCpin) == GPIO.LOW):
                	reading += 1
        	return reading 
	while True: 
        	print RCtime(18)
	
except KeyboardInterrupt:
	print "You've exited the program"
finally:
	GPIO.cleanup()

