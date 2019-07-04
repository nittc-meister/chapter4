import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

while True:
     GPIO.output(14, True)
     time.sleep(0.5)
     GPIO.output(14, False)
     time.sleep(0.5)

GPIO.cleanup()
