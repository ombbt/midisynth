#! /usr/bin/python
import RPi.GPIO as GPIO
#from machine import Pin
from pad4pi import rpi_gpio
#from evdev import UInput, ecodes as e



cols = [26, 10, 9, 11]
rows = [25, 24, 23, 18]
# rows = [18, 23, 24, 25]

keymap = [
	["1",	"2",	"3",	"A"],
	["4",	"5",	"6",	"B"],
	["7",	"8",	"9",	"C"],
	["0",	"F",	"E",	"D"]
]


GPIO.setmode(GPIO.BCM)
GPIO.setup(rows, GPIO.OUT)
GPIO.setup(cols, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("bonjour")


pressed = set()
while True:
	syn = False
	for i in range(len(rows)):
		GPIO.setup(rows[i], GPIO.OUT, initial = GPIO.LOW)
		for j in range(len(cols)):
			keycode = i * len(cols) +j
			newval = GPIO.input(cols[j]) == GPIO.LOW
			keypressed = keymap[j][i]
		
			syn = True
			if newval and not keycode in pressed:
				pressed.add(keycode)
				print(keypressed)
		
			elif not newval and keycode in pressed:
				pressed.discard(keycode)
				syn = True
				print("2", keypressed)
		GPIO.setup(rows[i], GPIO.IN)
		
