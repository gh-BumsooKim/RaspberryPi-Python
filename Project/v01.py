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

GPIO.setup(Ultra_TRGI, GPIO.OUT)
GPIO.setup(Ultra_ECHO, GPIO.IN)


print("set env----------------------")

GPIO.output(Ultra_TRGI, False)
time.sleep(0.1)

# Varible set



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
    
    #print("Distance : %.1f cm" %distance)
    
    #if(distance < 30){}
    
    time.sleep(0.5)
    
    
#display.lcd_display_string(" " , 1)