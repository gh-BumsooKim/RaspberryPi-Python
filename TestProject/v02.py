import RPi.GPIO as GPIO
import lcddriver
import time

# set env

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

display = lcddriver.lcd()

# GPIO PIN setup 

Ultra_TRGI = 20
Ultra_ECHO = 21

PIR_sensor = 16

LED = 12

LED_strip = 14

GPIO.setup(Ultra_TRGI, GPIO.OUT)
GPIO.setup(Ultra_ECHO, GPIO.IN)
GPIO.setup(LED_strip, GPIO.OUT)

print("set env----------------------")

GPIO.output(Ultra_TRGI, False)
time.sleep(0.1)

# Varible set


# Main OUTPUT

GPIO.output(LED_strip,1)

# Main Loop

while True:
    #Ultrasonic sensor output
    GPIO.output(Ultra_TRGI, True)
    time.sleep(0.00001)
    GPIO.output(Ultra_TRGI, False)
    while GPIO.input(Ultra_ECHO) == 0:   #time start
        start = time.time()
    while GPIO.input(Ultra_ECHO) == 1:   #time stop
        stop = time.time()
    
    check_time = stop - start
    distance = check_time*34300/2        #distance is (cm)
    st=str(distance)    
    
    display.lcd_display_string(st, 1)
    
    #print("Distance : %.1f cm" %distance)
    
    #if(distance < 30){}
    
    time.sleep(0.5)    
