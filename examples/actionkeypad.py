
#! /usr/bin/python
import RPi.GPIO as GPIO
#from machine import Pin
from pad4pi import rpi_gpio
import time
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

status = [1, 2, 3, 10, 4, 5, 6, 11, 7, 8, 9, 12, 0, 13, 14, 15]


GPIO.setmode(GPIO.BCM)
GPIO.setup(rows, GPIO.OUT)
GPIO.setup(cols, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("bonjour")


#def switch(action):
#	if action

#secs = 0
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
				print(keypressed, keycode)
				if keycode == 0:
					print('action 1')
				elif keycode == 1:
					print('action 4')
				elif keycode == 2:
					print('action 7')
				elif keycode == 3:
					print('action 0')
				elif keycode == 4:
					print('action 2')
				elif keycode == 5:
					print('action 5')
				elif keycode == 6:
					print('action 8')
				elif keycode == 7:
					print('action F')
				elif keycode == 8:
					print('action 3')
				elif keycode == 9:
					print('action 6')
				elif keycode == 10:
					print('action 9')
				elif keycode == 11:
					print('action E')
				elif keycode == 12:
					print('action A')
				elif keycode == 13: 
					print('action B')
				elif keycode == 14:
					print('action C')
				elif keycode == 15:
					print('action D')
					timmer = time.process_time()
					print(timmer)
			#	status[keypressed] = True
			#	print("statuspressed", keypressed, status[keypressed])
			elif not newval and keycode in pressed:
				pressed.discard(keycode)
			#	status[keypressed] = False
				syn = True
				print("raellllaesed") #, keypressed, keycode)
				timmer2 = time.process_time() -4 
				if keycode == 15 and timmer2 > timmer:
					print('action on release with timmer', timmer2)
					print('autodesctruction')
					print('explosed')
		GPIO.setup(rows[i], GPIO.IN)
		
