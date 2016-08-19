import RPi.GPIO as GPIO
import time

try:

	GPIO.setmode(GPIO.BCM)
	button = 19
	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	led = 17
	led2 = 23
	GPIO.setup(led, GPIO.OUT)
	GPIO.setup(led2, GPIO.OUT)
	while True:
		input_state = GPIO.input(button)
		if input_state == False:
			print('Button Pressed')
			time.sleep(0.2)
			GPIO.output(led, 1)
			time.sleep(0.5)
			GPIO.output(led2, 1)
		else: 
			GPIO.output(led, 0)
			GPIO.output(led2, 0)
except KeyboardInterrupt:
	print "You've exited the program"
finally:
	GPIO.cleanup()

