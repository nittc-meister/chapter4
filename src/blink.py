import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

i = 0
while True:
	GPIO.output(14, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(14, GPIO.LOW)
	time.sleep(1)
	i += 1
	if (i ==10):
		break

GPIO.cleanup()