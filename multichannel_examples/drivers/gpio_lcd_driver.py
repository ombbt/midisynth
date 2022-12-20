# Control an LCD 1602 display from Raspberry Pi with Python programming

#!/usr/bin/python

# Pinout of the LCD:
# 1 : GND
# 2 : 5V power
# 3 : Display contrast - Connect to middle pin potentiometer 
# 4 : RS (Register Select)
# 5 : R/W (Read Write) - Ground this pin (important)
# 6 : Enable or Strobe
# 7 : Data Bit 0 - data pin 0, 1, 2, 3 are not used
# 8 : Data Bit 1 - 
# 9 : Data Bit 2 - 
# 10: Data Bit 3 - 
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V
# 16: LCD Backlight GND

import RPi.GPIO as GPIO
from time import sleep

# GPIO to LCD mapping
LCD_RS = 7 # Pi pin 26
LCD_E = 8 # Pi pin 24
LCD_D4 = 25 # Pi pin 22
LCD_D5 = 24 # Pi pin 18
LCD_D6 = 23 # Pi pin 16
LCD_D7 = 18 # Pi pin 12

# Device constants
LCD_CHR = True # Character mode
LCD_CMD = False # Command mode
LCD_CHARS = 16 # Characters per line (16 max)
LCD_LINE_1 = 0x80 # LCD memory location for 1st line
LCD_LINE_2 = 0xC0 # LCD memory location 2nd line


class GpioLcd:
	# Initialize and clear display
	def __init__(self):	
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM) # Use BCM GPIO numbers
		GPIO.setup(LCD_E, GPIO.OUT) # Set GPIO's to output mode
		GPIO.setup(LCD_RS, GPIO.OUT)
		GPIO.setup(LCD_D4, GPIO.OUT)
		GPIO.setup(LCD_D5, GPIO.OUT)
		GPIO.setup(LCD_D6, GPIO.OUT)
		GPIO.setup(LCD_D7, GPIO.OUT)
		
		self.lcd_write(0x33,LCD_CMD) # Initialize
		self.lcd_write(0x32,LCD_CMD) # Set to 4-bit mode
		self.lcd_write(0x06,LCD_CMD) # Cursor move direction
		self.lcd_write(0x0C,LCD_CMD) # Turn cursor off
		self.lcd_write(0x28,LCD_CMD) # 2 line display
		self.lcd_write(0x01,LCD_CMD) # Clear display
		sleep(0.0005) # Delay to allow commands to process

	def lcd_write(self, bits, mode):
		# High bits
		GPIO.output(LCD_RS, mode) # RS

		GPIO.output(LCD_D4, False)
		GPIO.output(LCD_D5, False)
		GPIO.output(LCD_D6, False)
		GPIO.output(LCD_D7, False)
		if bits&0x10==0x10:
			GPIO.output(LCD_D4, True)
		if bits&0x20==0x20:
			GPIO.output(LCD_D5, True)
		if bits&0x40==0x40:
			GPIO.output(LCD_D6, True)
		if bits&0x80==0x80:
			GPIO.output(LCD_D7, True)

		# Toggle 'Enable' pin
		self.lcd_toggle_enable()

		# Low bits
		GPIO.output(LCD_D4, False)
		GPIO.output(LCD_D5, False)
		GPIO.output(LCD_D6, False)
		GPIO.output(LCD_D7, False)
		if bits&0x01==0x01:
			GPIO.output(LCD_D4, True)
		if bits&0x02==0x02:
			GPIO.output(LCD_D5, True)
		if bits&0x04==0x04:
			GPIO.output(LCD_D6, True)
		if bits&0x08==0x08:
			GPIO.output(LCD_D7, True)

		# Toggle 'Enable' pin
		self.lcd_toggle_enable()

	def lcd_toggle_enable(self):
		sleep(0.0005)
		GPIO.output(LCD_E, True)
		sleep(0.0005)
		GPIO.output(LCD_E, False)
		sleep(0.0005)

	def lcd_display_string(self, message, line):
		# Send text to display
		message = message.ljust(LCD_CHARS," ")

		self.lcd_write(line, LCD_CMD)

		for i in range(LCD_CHARS):
			self.lcd_write(ord(message[i]),LCD_CHR)


