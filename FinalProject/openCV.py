from flask import Flask, request
from flask import render_template
import RPi.GPIO as GPIO
import lcddriver
import time, datetime
import cv2
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--video', help='Input video path')
args = parser.parse_args()

cap = cv2.VideoCapture(args.video if args.video else 0)

time.sleep(3)

# Grap background image from first part of the video
for i in range(60):
  ret, background = cap.read()

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out = cv2.VideoWriter('videos/output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (background.shape[1], background.shape[0]))
out2 = cv2.VideoWriter('videos/original.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), (background.shape[1], background.shape[0]))

# set env
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

app = Flask(__name__)

display = lcddriver.lcd()

# GPIO PIN setup 
Ultra_TRGI = 20
Ultra_ECHO = 21

LED = 16
BUZZER = 26
MOTOR = 19

GPIO.setup(Ultra_TRGI, GPIO.OUT)
GPIO.setup(Ultra_ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(MOTOR, GPIO.OUT)

print("set env----------------------")

GPIO.output(Ultra_TRGI, False)
time.sleep(0.1)

# varible set
p = GPIO.PWM(BUZZER,100)
Frq = [300]
buzzer_speed = 0.5

servo = GPIO.PWM(MOTOR, 50)

# Main set
#servo.start(0)

@app.route("/")
def hello():
    return render_template("index.html")
    return "SMART HOME"

@app.route("/turn/left")
def servo_trunL():
    try:
        servo.start(0)
        servo.ChangeDutyCycle(3.5)
        time.sleep(0.5)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/turn/right")
def servo_turnR():
    try:
        servo.start(0)
        servo.ChangeDutyCycle(1.5)
        time.sleep(0.5)
        return "ok"
    except expression as identifier:
        return "fail"

@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO CLEAN UP"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="7894", debug=True) #localhost

try:
    while (cap.isOpened()):
        ret, img = cap.read()
        if not ret:
            break
        
        # Convert the color space from BGR to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Generate mask to detect red color
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask1 = mask1 + mask2

          # lower_black = np.array([0, 0, 0])
          # upper_black = np.array([255, 255, 80])
          # mask1 = cv2.inRange(hsv, lower_black, upper_black)

          # Remove noise
        mask_cloak = cv2.morphologyEx(mask1, op=cv2.MORPH_OPEN, kernel=np.ones((3, 3), np.uint8), iterations=2)
        mask_cloak = cv2.dilate(mask_cloak, kernel=np.ones((3, 3), np.uint8), iterations=1)
        mask_bg = cv2.bitwise_not(mask_cloak)

        cv2.imshow('mask_cloak', mask_cloak)

          # Generate the final output
        res1 = cv2.bitwise_and(background, background, mask=mask_cloak)
        res2 = cv2.bitwise_and(img, img, mask=mask_bg)
        result = cv2.addWeighted(src1=res1, alpha=1, src2=res2, beta=1, gamma=0)

        cv2.imshow('res1', res1)

          # cv2.imshow('ori', img)
        cv2.imshow('result', result)
        out.write(result)
        out2.write(img)
        
        if cv2.waitKey(1) == ord('q'):
            break
        #Ultrasonic sensor output
        GPIO.output(Ultra_TRGI, True)
        #time.sleep(0.00001)
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
            #time.sleep(speed)
        else:
            speed = 0.5
            p.stop()
    
        #main loop sleep
        #time.sleep(0.5)    

except KeyboardInterrupt:
    print("Cleaning UP")
    GPIO.cleanup
    display.lcd_clear()
    p.stop()
    servo.stop()
        
out.release()
out2.release()
cap.release()

#Web Server Button function
def servo_turnL():
    servo.ChangeDutyCycle(3.5)
    time.sleep(0.5)
    
def servo_turnR():
    servo.ChangeDutyCycle(1.5)
    time.sleep(0.5)