import RPi.GPIO as GPIO
from pad4pi import rpi_gpio

KEYPAD = [
	["1", "2", "3", "A"],
	["4", "5", "6", "B"],
	["7", "8", "9", "C"],
	["0", "F", "E", "D"]
]

#ROW_PINS = [18, 23]
#COL_PINS = [4, 17]

ROW_PINS = [23, 24, 25]
COL_PINS = [4, 17, 27, 22]


factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)
GPIO.setwarnings(False)



def print_key(key):
	print(key)

keypad.registerKeyPressHandler(print_key)
