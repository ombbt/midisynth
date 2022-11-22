#! /usr/bin/env python
import drivers
from time import sleep

display = drivers.Lcd()
try:
	while True:
		print("bonjour")
		display.lcd_display_string("bonjour", 1)
		display.lcd_display_string("prout", 2)

except Keyboardinterrupt:
	print("exit")
	display.lcd_clear()
