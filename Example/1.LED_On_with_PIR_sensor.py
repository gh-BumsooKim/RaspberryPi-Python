import RPi.GPIO as GPIO
import time

sensor = 4
LED = 8
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

print("Detect Ready~!")
time.sleep(3)

try:
    while True:
        if GPIO.input(sensor) == 1:
            print("Detect!")
			GPIO.output(LED, 1)
            time.sleep(1)
        if GPIO.input(sensor) == 0:
			GPIO.output(LED, 0)
            time.sleep(0.2)
        
except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup