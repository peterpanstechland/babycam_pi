#!python3
#coding:utf8

import RPi.GPIO as GPIO
import dht11
import time
import datetime
import codecs

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 4
instance = dht11.DHT11(pin=4)

result = instance.read()
if result.is_valid():
	with codecs.open('/dev/shm/mjpeg/user_annotate.txt', 'w', encoding='utf-8') as f:
		f.write("温度: %d" % result.temperature + "C 湿度: %d" % result.humidity + "% 更新温湿度时间: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  + "\n")
