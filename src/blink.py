import time
import RPi.GPIO as GPIO

PIN=14

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
    GPIO.output(PIN,True)
    time.sleep(1.0)
    GPIO.output(PIN,False)
    time.sleep(1.0)
GPIO.cleanup()
