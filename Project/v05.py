# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 03:31:42 2020

@author: 82109
"""


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

LED = 16

LED_strip = 14

BUZZER = 26

MOTOR = 19

GPIO.setup(Ultra_TRGI, GPIO.OUT)
GPIO.setup(Ultra_ECHO, GPIO.IN)
GPIO.setup(LED_strip, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)

print("set env----------------------")

GPIO.output(Ultra_TRGI, False)
time.sleep(0.1)

# Varible set

p = GPIO.PWM(BUZZER,100)
Frq = [263,294,330,349,392,440,493,523]
buzzer_speed = 0.5

servo = GPIO.PWM(MOTOR, 50)
servo.start(0)

# Main set

p.start(10)

# Main Loop
try:
    while True:
        #SERVO
        #servo.ChangeDutyCycle(7.5)
        #time.sleep(1)
        
        #BUZZER
        #for i in Frq:
        #        p.ChangeFrequency(i)
        #        time.sleep(buzzer_speed)
        
        
        #LED_Strip On
        #GPIO.output(LED_strip,1)
        
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
        st=str(int(distance))
        
        display.lcd_clear()
        display.lcd_display_string(st + "CM ", 1)
        
        print("Distance : %.1f cm" %distance)
        
        #if(distance < 30):
        #    GPIO.output(LED,1)
        #else:
        #    GPIO.output(LED,0)
        
        time.sleep(0.5)    

except KeyboardInterrupt:
    print("Cleaning UP")
    GPIO.cleanup
    display.lcd_clear()
    p.stop()
    servo.stop()
    
    
def servo_turnL():
    servo.ChangeDutyCycle(3.5)
    time.sleep(0.5)
    
def servo_turnR():
    servo.ChangeDutyCycle(1.5)
    time.sleep(0.5)