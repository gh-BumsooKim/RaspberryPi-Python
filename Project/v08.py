import RPi.GPIO as GPIO
import lcddriver
import time, datetime

# set env
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

display = lcddriver.lcd()

# GPIO PIN setup 
Ultra_TRGI = 20
Ultra_ECHO = 21

LED = 16
BUZZER = 26
MOTOR = 19

angle = 2.5

GPIO.setup(Ultra_TRGI, GPIO.OUT)
GPIO.setup(Ultra_ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(MOTOR, GPIO.OUT)

print("set env----------------------")

GPIO.output(Ultra_TRGI, False)
time.sleep(0.1)

# varible set
p = GPIO.PWM(BUZZER,100)
Frq = [300, 0]
buzzer_speed = 0.5

servo = GPIO.PWM(MOTOR, 50)

# Main set
servo.start(0)

# Main Loop
try:
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
        
        print("Distance : %.1f cm" %distance)
        
        #LCD output
        st=str(int(distance))
        
        display.lcd_clear()
        display.lcd_display_string("Distance : " + st + "CM", 1)
        
        #if(distance < 30):
        #    GPIO.output(LED,1)
        #else:
        #    GPIO.output(LED,0)
        
        if(distance < 50):
            display.lcd_display_string("Who are You!!!", 2)
            
            p.start(10)
            #is detect min 50 CM
            #for i in Frq:
                #p.ChangeFrequency(i)
                speed = distance*0.1
                time.sleep(speed)
        else:
            speed = 0.5
            p.stop()
        
        #main loop sleep
        time.sleep(0.5)    

except KeyboardInterrupt:
    print("Cleaning UP")
    GPIO.cleanup
    display.lcd_clear()
    p.stop()
    servo.stop()

#Web Server Button function
def servo_turnL():
    angle = angle + 1
    servo.ChangeDutyCycle(angle)
    time.sleep(0.5)
    
def servo_turnR():
    angle = angle - 1
    servo.ChangeDutyCycle(angle)
    time.sleep(0.5)