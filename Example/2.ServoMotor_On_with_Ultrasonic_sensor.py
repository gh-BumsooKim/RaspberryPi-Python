import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRGI = 23
ECHO = 24
SERVO_PIN = 12
print("Distance measurement with Ultrasonic")

GPIO.setup(TRGI, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)


GPIO.output(TRGI, False)
print("Waiting for sensor to settle")
time.sleep(2)
servo.start(0)

try:
    while True:
        GPIO.output(TRGI, True)
        time.sleep(0.00001)
        GPIO.output(TRGI, False)
        while GPIO.input(ECHO) == 0:
            start = time.time()
        while GPIO.input(ECHO) == 1:
            stop = time.time()
        check_time = stop - start
        distance = check_time*34300/2
        print("Distance : %.1f cm" %distance)
		if(Distance < 30)
		{
			servo.ChangeDutyCycle(12.5)
			time.sleep(1)
		}
        time.sleep(0.4)

except KeyboardInterrupt:
	servo.stop()
    print("Measuremenet stopped by User")
    GPIO.cleanup()