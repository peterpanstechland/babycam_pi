import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
state = GPIO.input(17)
if state == True:
	GPIO.output(17,GPIO.LOW)
	print('off')
else:
	GPIO.output(17,GPIO.HIGH)
	print('on')
#time.sleep(1)
#print "LED off"
#GPIO.output(2,GPIO.LOW)
