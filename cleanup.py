import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

for pin in range(28):
	try:
		GPIO.setup(pin, GPIO.IN) #sets all pins 1-28 as input 
	except RuntimeError:
		pass

GPIO.cleanup()
