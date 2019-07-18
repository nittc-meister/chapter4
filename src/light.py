import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

GPIO.output(14, GPIO.HIGH)
time.sleep(1000)
GPIO.output(14,GPIO.LOW)

GPIO.cleanup()
