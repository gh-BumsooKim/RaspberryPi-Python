### using GPIO.setmode(_GPIO.BCM_) / not BOARD setmode

File 1 : set up PIN 4 to GPIO.IN, set up PIN 8 to GPIO.OUT 

→ PIN 4 is used to read INPUT at PIR sensor. PIN 8 is used to send OUTPUT to LED 

File 2 : set up PIN 23 to GPIO.OUT, set up PIN 23 to GPIO.IN, set up PIN 12 to GPIO.OUT

→ PIN 23, PIN 24 is used to operate Ultrasonic sensor. PIN 12 is used to operate ServoMotor

(but you can use any other GPIO PIN instead of GPIO PIN, such as PIN 4, and PIN 8 in File 1)
