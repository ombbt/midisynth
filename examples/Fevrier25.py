
from mididings import *
from mididings.event import *
from mididings.extra import *
from mididings.engine import *
import os
import drivers
import RPi.GPIO as GPIO
import time
from smbus import SMBus
from subprocess import call

#LCD display
display = drivers.Lcd()
display.lcd_display_string("     bonjour    ", 1)
display.lcd_display_string("      zen!!     ", 2)

#arduino i2C adresse
addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1


#Keypad
cols = [26, 10, 9, 11]
rows = [25, 24, 23, 20]

keymap = [
	["1", "2", "3", "A"],
	["4", "5", "6", "B"],
	["7", "8", "9", "C"],
	["0", "F", "E", "D"]
]
GPIO.setmode(GPIO.BCM)
GPIO.setup(rows, GPIO.OUT)
GPIO.setup(cols, GPIO.IN, pull_up_down = GPIO.PUD_UP)

print("config GPIO OK")
#print(TRANSPOSE)

pressed = set()
timmer1 = 1.0
timmer2 = 1.0
offset = 0
mode = False
lightonoff = False
pianomodenumber = 0
organmodenumber = 0
bassemodenumber = 0
synthmodenumber = 0

def transposescene():
	global offset
	if offset == 0:
		switch_scene(30, subscene=None)
		print("transpose scene 0")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:0  ", 2)

	elif offset == 1:
		switch_scene(31, subscene=None)
		print("t1")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:1 ", 2)
	elif offset == 2:
		switch_scene(32, subscene=None)
		print("t2")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:2 ", 2)
	elif offset == 3:
		switch_scene(33, subscene=None)
		print("t3")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:3 ", 2)
	elif offset == 4:
		switch_scene(34, subscene=None)
		print("t4")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:4 ", 2)
	elif offset == 5:
		switch_scene(35, subscene=None)
		print("t5")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:5 ", 2)
	elif offset == 6:
		switch_scene(36, subscene=None)
		print("t6")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:6 ", 2)
	elif offset == 7:
		switch_scene(37, subscene=None)
		print("t7")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:7 ", 2)
	elif offset == 8:
		switch_scene(38, subscene=None)
		print("t8")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:8 ", 2)
	elif offset == 9:
		switch_scene(39, subscene=None)
		print("t9")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:9 ", 2)
	elif offset == 10:
		switch_scene(40, subscene=None)
		print("t10")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:10", 2)
	elif offset == 11:
		switch_scene(41, subscene=None)
		print("t11")
		display.lcd_display_string(" transpose mode ", 1)
		display.lcd_display_string("m:2  tr:11", 2)

def pianomode():
	global pianomodenumber
	if pianomodenumber == 0:
		switch_scene(50, subscene=None)
		#print("pianomode")
		display.lcd_display_string("0:0 YGrandpiano", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
#		pianomodenumber = 1

	if pianomodenumber == 1:
		switch_scene(51, subscene=None)
		#print("transpose scene 0")
		display.lcd_display_string("0:1 Bightpiano ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
#		pianomodenumber = 2

	if pianomodenumber == 2:
		switch_scene(52, subscene=None)
		#print("transpose scene 0")
		display.lcd_display_string("0:2 Electric.p ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
#		pianomodenumber = 3

	if pianomodenumber == 3:
		switch_scene(53, subscene=None)
		#print("transpose scene 0")
		display.lcd_display_string("0:3 E.Piano 1  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
#		pianomodenumber = 4

	if pianomodenumber == 4:
		switch_scene(54, subscene=None)
		#print("transpose scene 0")
		display.lcd_display_string("0:4 Rhodes Ep  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
		pianomodenumber = 0
	elif pianomodenumber == 0:
		pianomodenumber = 1

	elif pianomodenumber == 1:
		pianomodenumber = 2

	elif pianomodenumber == 2:
		pianomodenumber = 3

	elif pianomodenumber == 3:
		pianomodenumber = 4
	

def organmode():
	global organmodenumber
	if organmodenumber == 0:
		switch_scene(60, subscene=None)
		display.lcd_display_string("0:30 Drawbarorgan", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 1:
		switch_scene(61, subscene=None)
		display.lcd_display_string("0:31 Rock organ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 2:
		switch_scene(62, subscene=None)
		display.lcd_display_string("0:32 organ 2     ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 3:
		switch_scene(63, subscene=None)
		display.lcd_display_string("0:33 organ 3     ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 4:
		switch_scene(64, subscene=None)
		display.lcd_display_string("0:34 organ 5     ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 5:
		switch_scene(65, subscene=None)
		display.lcd_display_string("0:35 HC2org2  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 6:
		switch_scene(66, subscene=None)
		display.lcd_display_string("0:36 HC2org2vib", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 7:
		switch_scene(67, subscene=None)
		display.lcd_display_string("0:37 HC2org1     ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 8:
		switch_scene(68, subscene=None)
		display.lcd_display_string("0:38 HC2org1vib  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 9:
		switch_scene(69, subscene=None)
		display.lcd_display_string("0:39 HC2org3perc  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 10:
		switch_scene(70, subscene=None)
		display.lcd_display_string("0:40 HC2org4    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 11:
		switch_scene(71, subscene=None)
		display.lcd_display_string("0:41 Hammond1    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if organmodenumber == 12:
		switch_scene(72, subscene=None)
		display.lcd_display_string("0:42 Churchorgan ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
		organmodenumber = 0

	elif organmodenumber == 0:
		organmodenumber = 1

	elif organmodenumber == 1:
		organmodenumber = 2

	elif organmodenumber == 2:
		organmodenumber = 3

	elif organmodenumber == 3:
		organmodenumber = 4

	elif organmodenumber == 4:
		organmodenumber = 5

	elif organmodenumber == 5:
		organmodenumber = 6

	elif organmodenumber == 6:
		organmodenumber = 7

	elif organmodenumber == 7:
		organmodenumber = 8

	elif organmodenumber == 8:
		organmodenumber = 9

	elif organmodenumber == 9:
		organmodenumber = 10

	elif organmodenumber == 10:
		organmodenumber = 11

	elif organmodenumber == 11:
		organmodenumber = 12



def synthmode():
	global synthmodenumber
	if synthmodenumber == 0:
		switch_scene(80, subscene=None)
		display.lcd_display_string("0:60 5th saw wave", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 1:
		switch_scene(81, subscene=None)
		display.lcd_display_string("0:61 014          ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if synthmodenumber == 2:
		switch_scene(82, subscene=None)
		display.lcd_display_string("0:62 016        ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 3:
		switch_scene(83, subscene=None)
		display.lcd_display_string("0:63 033        ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 4:
		switch_scene(84, subscene=None)
		display.lcd_display_string("0:64 tubular bells", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if synthmodenumber == 5:
		switch_scene(85, subscene=None)
		display.lcd_display_string("0:65 080         ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 6:
		switch_scene(86, subscene=None)
		display.lcd_display_string("0:66 vibes6     ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 7:
		switch_scene(87, subscene=None)
		display.lcd_display_string("0:67 024      ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 8:
		switch_scene(88, subscene=None)
		display.lcd_display_string("0:68 Basicmonologue", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 9:
		switch_scene(89, subscene=None)
		display.lcd_display_string("0:69 arcleadmonologue", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 10:
		switch_scene(90, subscene=None)
		display.lcd_display_string("0:70 morse monologue", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 11:
		switch_scene(91, subscene=None)
		display.lcd_display_string("0:71 violin    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 12:
		switch_scene(92, subscene=None)
		display.lcd_display_string("0:72 HC2ramdom", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 13:
		switch_scene(93, subscene=None)
		display.lcd_display_string("0:73 Trombonne", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 14:
		switch_scene(94, subscene=None)
		display.lcd_display_string("0:74 Brass section", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 15:
		switch_scene(95, subscene=None)
		display.lcd_display_string("0:75 Saw wave  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 16:
		switch_scene(96, subscene=None)
		display.lcd_display_string("0:76 Fifth sawtooph", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 17:
		switch_scene(97, subscene=None)
		display.lcd_display_string("0:77 square Lead  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 18:
		switch_scene(98, subscene=None)
		display.lcd_display_string("0:78 sweep pad   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 19:
		switch_scene(99, subscene=None)
		display.lcd_display_string("0:79 Brightness    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 20:
		switch_scene(100, subscene=None)
		display.lcd_display_string("0:80 Halo Pad    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 21:
		switch_scene(101, subscene=None)
		display.lcd_display_string("0:81 Vox 3       ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 22:
		switch_scene(102, subscene=None)
		display.lcd_display_string("0:82 saturn      ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 23:
		switch_scene(103, subscene=None)
		display.lcd_display_string("0:83 Synthbrass3", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 24:
		switch_scene(104, subscene=None)
		display.lcd_display_string("0:84 sine wave    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 25:
		switch_scene(105, subscene=None)
		display.lcd_display_string("0:85 Feedbackguitar", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 26:
		switch_scene(106, subscene=None)
		display.lcd_display_string("0:86 guitarfeedback", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 27:
		switch_scene(107, subscene=None)
		display.lcd_display_string("0:87 Orchestralpad", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if synthmodenumber == 28:
		switch_scene(108, subscene=None)
		display.lcd_display_string("0:88 Mandolin", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 29:
		switch_scene(109, subscene=None)
		display.lcd_display_string("0:89 vide     ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 30:
		switch_scene(110, subscene=None)
		display.lcd_display_string("0:90 siren    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 31:
		switch_scene(111, subscene=None)
		display.lcd_display_string("0:91 m.loguesiren", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 32:
		switch_scene(112, subscene=None)
		display.lcd_display_string("0:92 m.sequencer", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 33:
		switch_scene(113, subscene=None)
		display.lcd_display_string("0:93 Drum synth", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 34:
		switch_scene(114, subscene=None)
		display.lcd_display_string("0:94 scrtach Scrape", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 35:
		switch_scene(115, subscene=None)
		display.lcd_display_string("0:95 Radio spike   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 36:
		switch_scene(116, subscene=None)
		display.lcd_display_string("0:96 sohba 62      ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 37:
		switch_scene(117, subscene=None)
		display.lcd_display_string("0:97 blue screen  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if synthmodenumber == 38:
		switch_scene(118, subscene=None)
		display.lcd_display_string("0:98 vide        ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
		synthmodenumber = 0

	elif synthmodenumber == 0:
		synthmodenumber = 1 

	elif synthmodenumber == 1:
		synthmodenumber = 2

	elif synthmodenumber == 2:
		synthmodenumber = 3

	elif synthmodenumber == 3:
		synthmodenumber = 4

	elif synthmodenumber == 4:
		synthmodenumber = 5

	elif synthmodenumber == 5:
		synthmodenumber = 6

	elif synthmodenumber == 6:
		synthmodenumber = 7

	elif synthmodenumber == 7:
		synthmodenumber = 8

	elif synthmodenumber == 8:
		synthmodenumber = 9

	elif synthmodenumber == 9:
		synthmodenumber = 10

	elif synthmodenumber == 10:
		synthmodenumber = 11

	elif synthmodenumber == 11:
		synthmodenumber = 12

	elif synthmodenumber == 12:
		synthmodenumber = 13

	elif synthmodenumber == 13:
		synthmodenumber = 14

	elif synthmodenumber == 14:
		synthmodenumber = 15

	elif synthmodenumber == 15:
		synthmodenumber = 16

	elif synthmodenumber == 16:
		synthmodenumber = 17

	elif synthmodenumber == 17:
		synthmodenumber = 18

	elif synthmodenumber == 18:
		synthmodenumber = 19

	elif synthmodenumber == 19:
		synthmodenumber = 20

	elif synthmodenumber == 20:
		synthmodenumber = 21

	elif synthmodenumber == 21:
		synthmodenumber = 22

	elif synthmodenumber == 22:
		synthmodenumber = 23

	elif synthmodenumber == 23:
		synthmodenumber = 24

	elif synthmodenumber == 24:
                synthmodenumber = 25

	elif synthmodenumber == 25:
		synthmodenumber = 26

	elif synthmodenumber == 26:
		synthmodenumber = 27

	elif synthmodenumber == 27:
		synthmodenumber = 28

	elif synthmodenumber == 28:
		synthmodenumber = 29

	elif synthmodenumber == 29:
		synthmodenumber = 30

	elif synthmodenumber == 30:
		synthmodenumber = 31

	elif synthmodenumber == 31:
		synthmodenumber =32

	elif synthmodenumber == 32:
		synthmodenumber = 33

	elif synthmodenumber == 33:
		synthmodenumber = 34

	elif synthmodenumber == 34: 
		synthmodenumber = 35

	elif synthmodenumber == 35:
		synthmodenumber = 36

	elif synthmodenumber == 36:
		synthmodenumber = 37

	elif synthmodenumber == 37:
		synthmodenumber = 38

def bassemode():
	global bassemodenumber
	if bassemodenumber == 0:
		switch_scene(120, subscene=None)
		display.lcd_display_string("0:10 Acoustic basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if bassemodenumber == 1:
		switch_scene(121, subscene=None)
		display.lcd_display_string("0:11 Finguerd basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 2:
		switch_scene(122, subscene=None)
		display.lcd_display_string("0:12 Fretless basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if bassemodenumber == 3:
		switch_scene(123, subscene=None)
		display.lcd_display_string("0:13 Fretless basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 4:
		switch_scene(124, subscene=None)
		display.lcd_display_string("0:14 Fingured basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 5:
		switch_scene(125, subscene=None)
		display.lcd_display_string("0:15 Picked basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 6:
		switch_scene(126, subscene=None)
		display.lcd_display_string("0:16 Fretlessbasse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 7:
		switch_scene(127, subscene=None)
		display.lcd_display_string("0:17 Slapbasse   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if bassemodenumber == 8:
		switch_scene(128, subscene=None)
		display.lcd_display_string("0:18 Popbasse   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 9:
		switch_scene(129, subscene=None)
		display.lcd_display_string("0:19 Realbasse   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 10:
		switch_scene(130, subscene=None)
		display.lcd_display_string("0:20 Studiobasse   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 11:
		switch_scene(131, subscene=None)
		display.lcd_display_string("0:21 Bass 74'basse", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 12:
		switch_scene(132, subscene=None)
		display.lcd_display_string("0:22 FunkyFrettlessb", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 13:
		switch_scene(133, subscene=None)
		display.lcd_display_string("0:23 MutedFretlessb  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 14:
		switch_scene(134, subscene=None)
		display.lcd_display_string("0:24 FilteredFretless", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 15:
		switch_scene(135, subscene=None)
		display.lcd_display_string("0:25 vide            ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 16:
		switch_scene(136, subscene=None)
		display.lcd_display_string("0:50 basse&Lead", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 17:
		switch_scene(137, subscene=None)
		display.lcd_display_string("0:51 Synth bass1   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 18:
		switch_scene(138, subscene=None)
		display.lcd_display_string("0:52 Synth bass2   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 19:
		switch_scene(139, subscene=None)
		display.lcd_display_string("0:53 basse&Lead", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 20:
		switch_scene(140, subscene=None)
		display.lcd_display_string("0:54 Sub data    ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)


	if bassemodenumber == 21:
		switch_scene(141, subscene=None)
		display.lcd_display_string("0:55 Vox8       ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 22:
		switch_scene(142, subscene=None)
		display.lcd_display_string("0:56 Synthbass4  ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 23:
		switch_scene(143, subscene=None)
		display.lcd_display_string("0:57 Saw Classic   ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)

	if bassemodenumber == 24:
		switch_scene(144, subscene=None)
		display.lcd_display_string("0:58 Vide          ", 1)
		display.lcd_display_string("m:2  tr:0 ", 2)
		bassemodenumber = 0

	elif bassemodenumber == 0:
		bassemodenumber = 1

	elif bassemodenumber == 1:
		bassemodenumber = 2

	elif bassemodenumber == 2:
		bassemodenumber = 3

	elif bassemodenumber == 3:
		bassemodenumber = 4

	elif bassemodenumber == 4:
		bassemodenumber = 5

	elif bassemodenumber == 5:
		bassemodenumber = 6

	elif bassemodenumber == 6:
		bassemodenumber = 7

	elif bassemodenumber == 7:
		bassemodenumber = 8

	elif bassemodenumber == 8:
		bassemodenumber = 9

	elif bassemodenumber == 9:
		bassemodenumber = 10

	elif bassemodenumber == 10:
		bassemodenumber = 11

	elif bassemodenumber == 11:
		bassemodenumber = 12

	elif bassemodenumber == 12:
		bassemodenumber = 13

	elif bassemodenumber == 13:
		bassemodenumber = 14

	elif bassemodenumber == 14:
		bassemodenumber = 15

	elif bassemodenumber == 15:
		bassemodenumber = 16

	elif bassemodenumber == 16:
		bassemodenumber = 17

	elif bassemodenumber == 17:
		bassemodenumber = 18

	elif bassemodenumber == 18:
		bassemodenumber = 19

	elif bassemodenumber == 19:
		bassemodenumber = 20

	elif bassemodenumber == 20:
		bassemodenumber = 21

	elif bassemodenumber == 21:
		bassemodenumber = 22

	elif bassemodenumber == 22:
		bassemodenumber = 23

	elif bassemodenumber == 23:
		bassemodenumber = 24


def readkeypad(self):
#	TRANSPOSE =int(os.getenv('TRANSPOSE'))
	global offset
	global lightonoff
	global mode
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
				if keycode == 0:  #Keypad '1'
					if mode == False:
						#initran = 5
						#tran = initran + offset
						#print(type(tran))
						#os.putenv(TRANSPOSE,4)      #ddlk
						#os.environ['TRANSPOSE'] = 2
						switch_scene(1, subscene=None)
						display.lcd_display_string("hit the road jack", 1)
						display.lcd_display_string("m:1  tr:5 ", 2)
						bus.write_byte(addr, 0x02)
						#print("TRANSPOSE= ", TRANSPOSE, "  initran=", initran, " offset= ", offset )
					elif mode == True:
						switch_scene(13, subscene=None)
						print('scene 13')
						display.lcd_display_string("aint no stop ", 1)
						display.lcd_display_string("m:2  chang  ", 2)

						switch_scene(13, subscene=None)
				elif keycode == 1:
					if mode == False:
						switch_scene(4, subscene=None)
						print("scene 4")
						display.lcd_display_string("  if you feel it  ", 1)
						display.lcd_display_string("m:1  tr:1 ", 2)
						bus.write_byte(addr, 0x05)

					elif mode == True:
						switch_scene(16, subscene=None)
						print("scene 16")
						display.lcd_display_string("  ladies night   ", 1)
						display.lcd_display_string("m:2  tr:  ", 2)

						#switch_scene(16, subscene=None)
					#switch_scene(4, subscene=None)
				elif keycode == 2:
					if mode == False:
						print("scene 7")
						display.lcd_display_string("   bad girls    ", 1)
						display.lcd_display_string("m:1  tr:10", 2)
						bus.write_byte(addr, 0x08)

						switch_scene(7, subscene=None)
					elif mode == True:
						print("scene 19 ")
						display.lcd_display_string("   get down   ", 1)
						display.lcd_display_string("m:2  tr:", 2)
						bus.write_byte(addr, 0x09)
						switch_scene(19, subscene=None)
 #config light de loose yourself to dance
						#switch_scene(19, subscene=None)
				elif keycode == 3:
					if mode == False:
						print("can't stand loosing you")
						display.lcd_display_string("   the police   ", 1)
						display.lcd_display_string("m:1  tr:10", 2)
						bus.write_byte(addr, 0x0B)
						switch_scene(10, subscene=None)
					elif mode == True:
						synthmode()

				elif keycode == 4:	#scene 2
					if mode == False:
						switch_scene(2, subscene=None)
						display.lcd_display_string("   billie jean  ", 1)
						display.lcd_display_string("m:1  tr:9", 2)
						bus.write_byte(addr, 0x03)
					elif mode == True:
						switch_scene(14, subscene=None)
						display.lcd_display_string(" diamond real    ", 1)
						display.lcd_display_string("m:2  tr:", 2)

						#switch_scene(, subscene=None)
				elif keycode == 5:
					if mode == False:
						#print("scene 5")
						display.lcd_display_string(" feel goood inc ", 1)
						display.lcd_display_string("m:1  tr:8 ", 2)
						bus.write_byte(addr, 0x06)
						switch_scene(5, subscene=None)
					elif mode == True:
						display.lcd_display_string("scen17 vide      ", 1)
						display.lcd_display_string("m:2  tr:", 2)
						print("scene 17")
						#switch_scene(, subscene=None)
				elif keycode == 6:
					if mode == False:
						print("scene 8")
						display.lcd_display_string("loose yourself danc", 1)
						display.lcd_display_string("m:1  tr:3 ", 2)
						bus.write_byte(addr, 0x09)

						switch_scene(8, subscene=None)
					elif mode == True:
						display.lcd_display_string("scene 20 vide    ", 1)
						display.lcd_display_string("m:2  tr:", 2)

						#switch_scene(, subscene=None)
				elif keycode == 7:
					if mode == False:
						print("scene F")
						display.lcd_display_string("   solo clean   ", 1)
						display.lcd_display_string("m:1  tr:5 ", 2)
						bus.write_byte(addr, 0x0C)
						switch_scene(11, subscene=None)
					elif mode == True:
						#display.lcd_display_string("  y.GRANPIANO   ", 1)
						#display.lcd_display_string("m:2  tr:0", 2)

						#switch_scene(23, subscene=None)
						#print("scene F mode 2 YAMAHA GRANPIANO")
						pianomode()
				elif keycode == 8: #scene 3
					if mode == False:
						display.lcd_display_string("    Automatic   ", 1)
						display.lcd_display_string("m:1  tr:7 ", 2)
						bus.write_byte(addr, 0x04)
						switch_scene(3, subscene=None)
					elif mode == True:
						print("scene15")
						display.lcd_display_string("     teckno    ", 1)
						display.lcd_display_string("m:2  tr:", 2)
						switch_scene(15, subscene=None)
						#switch_scene(, subscene=None)
				elif keycode == 9:
					if mode == False:
						display.lcd_display_string("the next episode", 1)
						display.lcd_display_string("m:1  tr:0 ", 2)
						bus.write_byte(addr, 0x07)
						print("scene 6")
						switch_scene(6, subscene=None)
					elif mode == True:
						bassemode()

				elif keycode == 10:
					if mode == False:
						print("scene 9")
						display.lcd_display_string("     finaly    ", 1)
						display.lcd_display_string("m:1  tr:0 ", 2)
						bus.write_byte(addr, 0x0A)
						switch_scene(9, subscene=None)
					elif mode == True:
						organmode()

				elif keycode == 11:
					if mode == False:
						print("scene E")
						display.lcd_display_string("   solo satu   ", 1)
						display.lcd_display_string("m:1  tr:0 ", 2)
						bus.write_byte(addr, 0x0D)
						switch_scene(12, subscene=None)
					elif mode == True:
						print("scene E mode2, Full Talkbox")
						switch_scene(24, subscene=None)
						display.lcd_display_string(" TalkBox Mode  ", 1)
						display.lcd_display_string("m:2  tr:0 ", 2)

				elif keycode == 12:
					display.lcd_display_string(" autodestruction  ", 2)
					#display.lcd_display_string("      !!!!       ", 2)
					bus.write_byte(addr, 0x00)
					#print("autodestruction")
					global timmer1
					timmer1 = time.process_time()
					timmer1 = timmer1 +0.09 
					print("timmer1", timmer1)
				elif keycode == 13:
					if mode == False:
						if lightonoff == False:
							lightonoff = True
							print("light On")
							display.lcd_display_string("m:1  tr:   li:ON   ", 2)
							bus.write_byte(addr, 0x01)

						elif lightonoff == True:
							lightonoff = False
							print("light Off")
							display.lcd_display_string("m:1  tr:   li:OFF   ", 2)
							bus.write_byte(addr, 0x00)

					elif mode == True:
						if offset < 11:
							offset = offset +1
							transposescene()
				elif keycode == 14: 
					if mode == False:
						print("banana")
						display.lcd_display_string("   Banana mode  ", 1)
						bus.write_byte(addr, 0x14)
					elif mode == True:
						if offset > 0:
							offset = offset -1
							transposescene()

				elif keycode == 15:
					if mode ==False:
						mode = True
						print("switch to mode 2")
						display.lcd_display_string("m:2  tr:", 2)

					elif mode == True:
						mode = False
						print("switch to mode 1")
						display.lcd_display_string("m:1  tr:", 2)

			elif not newval and keycode in pressed:
				pressed.discard(keycode)
				syn = True
				#	print('relaese')
				global timmer2
				timmer2 = time.process_time()
				#print("timmer1:", timmer1)
				#print("timmer2:", timmer2)
				if keycode == 12 and timmer2 > timmer1:
					print("explosed")
					display.lcd_display_string("    EXPLOSED    ", 1)
					display.lcd_display_string("################", 2)
					call(['shutdown -h now'], shell=True)

		GPIO.setup(rows[i], GPIO.IN)


config(
	backend='alsa',
	client_name='mididings',
	in_ports = [	('Launchkey MK3 49 LKMK3 MIDI IN', '24:0'),
			('Arduino Leonardo MIDI 1', '20:0')
			
		],
	out_ports = [
	('Launchkey MK3 49 LKMK3 DAW IN','24:1'),
        ('mididings output','128:0')	],
)

#pre= Filter(~CTRL) % Print('input', portnames='in')  // ~Filter(PROGRAM)
pre = Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 

control = [ 
	Process(readkeypad),
#	Filter(PROGRAM) >> SceneSwitch(scenenumber)
]
 # SceneSwitch()
	 



  #crée le programe control Filter(PROGRAM) et SceneSwitch() sont des fonction existantes, voir doc mididings
	#	pre = Print('input', portname='in') >> ~Filter(PROGRAM)
#pre = Print()

#definie les sounds/output
out1 = Output('mididings output', 1)  #channel 1 clavier principal on port 'FLUID synth
out2 = Output('mididings output', 2)  #talkbox
out3 = Output('mididings output', 3) #2em clavier si channelssplit
out4 = Output('mididings output', 4) #basse
out5 = Output('mididings output', 5) #pads
out6 = Output('mididings output', 6) #pads
out7 = Output('mididings output', 7) #pads
out8 = Output('mididings output', 8) #2em son du clavier basse
out10 = Output('mididings output', 10) #channel "10" percussions

launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)
launchkeydaw10 = Output('Launchkey MK3 49 LKMK3 DAW IN',10)
launchkeydaw12 = Output('Launchkey MK3 49 LKMK3 DAW IN',12)

#Gestion des lumierres avec les pads
def light1(self):
	print("light1, 0x80")
	bus.write_byte(addr, 0x80)
def light2(self):
	print("light2, 0x82")
	bus.write_byte(addr, 0x81)
def light3(self):
	print("light3")
	bus.write_byte(addr, 0x90)
def light4(self):
	print("light4")
	bus.write_byte(addr, 0x91)
def light5(self):
	print("light5")
	bus.write_byte(addr, 0x92)
def light6(self):
	print("light6")
	bus.write_byte(addr, 0x82)
def light7(self):
	print("light7")
	bus.write_byte(addr, 0x83)
def light8(self):
	print("light8")
	bus.write_byte(addr, 0x94)
def light9(self):
	print("light9")
	bus.write_byte(addr, 0x95)
def light10(self):
	print("light10")
	bus.write_byte(addr, 0x96)
def light11(self):
        print("light10")
        bus.write_byte(addr, 0x97)
def light12(self):
        print("light10")
        bus.write_byte(addr, 0x98)

def lightkick(self):
	bus.write_byte(addr, 0xA0)

def lightsym(self):
	bus.write_byte(addr, 0xA1)

def talkbox(self, togle):
	if togle == True:
		print("talkboxlight ON")
		print("talkboxMic Activate")
		bus.write_byte(addr, 0xA2)
	elif togle == False:
		print("talkboxlight OFF")
		print("talkboxMic Unactivate")
		bus.write_byte(addr, 0xA3)



newpadsdf = [
	#NotesPads HAHAHHAHAHAHHAHAHAHAAA process light 1 a 10
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True)

	#lightspad
	CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
	CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
	CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
	CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
	CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
	CtrlFilter(49) >> CtrlValueFilter(127) >> Process(light6),
	CtrlFilter(50) >> CtrlValueFilter(127) >> Process(light7),
	CtrlFilter(51) >> CtrlValueFilter(127) >> Process(light8),



	CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light9),
	CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light5),
	CtrlFilter(38) >> CtrlValueFilter(127) >> NoteOn(33, 60) >> out7,
	CtrlFilter(39) >> CtrlValueFilter(127) >> NoteOn(24, 65) >> out8,
	CtrlFilter(40) >> CtrlValueFilter(127) >> [NoteOn(30, 60) >> out3, Process(light11)],
	CtrlFilter(41) >> CtrlValueFilter(127) >> [NoteOn(43, 60) >> out3, Process(light12)],
	CtrlFilter(42) >> CtrlValueFilter(127) >> NoteOn(60, 80) >> out6,
	CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(27, 80) >> out5,
#	CtrlFilter(43) >> CtrlValueFilter(0) >> NoteOff(34, 0) >>out5,
]

getdownpads = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA process light 1 a 10
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True)

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(49) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(50) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(51) >> CtrlValueFilter(127) >> Process(light8),



        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light9),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(38) >> CtrlValueFilter(127) >> NoteOn(33, 60) >> out7,
        CtrlFilter(39) >> CtrlValueFilter(127) >> NoteOn(24, 60) >> out8,
        CtrlFilter(40) >> CtrlValueFilter(127) >> [NoteOn(34, 60) >> out3, Process(light11)],
        CtrlFilter(41) >> CtrlValueFilter(127) >> [NoteOn(48, 60) >> out3, Process(light12)],
        CtrlFilter(42) >> CtrlValueFilter(127) >> NoteOn(62, 70) >> out6,
        CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(32, 80) >> out5,
#       CtrlFilter(43) >> CtrlValueFilter(0) >> NoteOff(34, 0) >>out5,
]

ifyoufeelpads = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA process light 1 a 10
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True)

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(49) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(50) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(51) >> CtrlValueFilter(127) >> Process(light8),



        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light8),
        CtrlFilter(40) >> CtrlValueFilter(127) >> NoteOn(32, 115) >> out8,
        CtrlFilter(41) >> CtrlValueFilter(127) >> NoteOn(36, 70) >> out5,
        CtrlFilter(42) >> CtrlValueFilter(127) >> [NoteOn(56, 60) >> out6, Process(light11)],
        CtrlFilter(43) >> CtrlValueFilter(127) >> [NoteOn(90, 60) >> out7, Process(light12)],
#       CtrlFilter(43) >> CtrlValueFilter(0) >> NoteOff(34, 0) >>out5,
]

finalypads = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA process light 1 a 10
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True)

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(49) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(50) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(51) >> CtrlValueFilter(127) >> Process(light8),



        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light8),
        CtrlFilter(40) >> CtrlValueFilter(127) >> NoteOn(34, 115) >> out7,
        CtrlFilter(41) >> CtrlValueFilter(127) >> NoteOn(32, 70) >> out5,
        CtrlFilter(42) >> CtrlValueFilter(127) >> NoteOn(49, 80) >> out6,
        CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(38, 80) >> out7,
#       CtrlFilter(43) >> CtrlValueFilter(0) >> NoteOff(34, 0) >>out5,
]

pads1 = [
	#NotesPads HAHAHHAHAHAHHAHAHAHAAA
#	CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
	CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(34, 110) >> out5,
	CtrlFilter(43) >> CtrlValueFilter(0) >> NoteOff(34, 0) >>out5,
	CtrlFilter(50) >> CtrlValueFilter(127) >> [NoteOn(54, 60) >> out6, Process(light11)],
	CtrlFilter(42) >> CtrlValueFilter(127) >> [NoteOn(90, 60) >> out7, Process(light12)],

	#lightspad
	CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
	CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
	CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
	CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
	CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
	CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light6),
	CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light7),
	CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light8),
	CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light9),
	CtrlFilter(40) >> CtrlValueFilter(127) >> Process(light10),
]


padsdf = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
        CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(36, 110) >> out5,
        CtrlFilter(50) >> CtrlValueFilter(127) >> [NoteOn(0, 60) >> out6, Process(light11)],
        CtrlFilter(42) >> CtrlValueFilter(127) >> [NoteOn(36, 60) >> out7, Process(light12)],

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light8),
        CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light9),
        CtrlFilter(40) >> CtrlValueFilter(127) >> Process(light10),
]



send_percu_i2c = [  	KeyFilter(36) >> Process(lightkick),
			KeyFilter(49) >> Process(lightsym),
]


padsdreal = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
        CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(82, 110) >> out5,
        CtrlFilter(50) >> CtrlValueFilter(127) >> [NoteOn(0, 60) >> out6, Process(light11)],
        CtrlFilter(42) >> CtrlValueFilter(127) >> [NoteOn(36, 60) >> out7, Process(light12)],

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light8),
        CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light9),
        CtrlFilter(40) >> CtrlValueFilter(127) >> Process(light10),
]


padspolice = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA
#      CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
#       CtrlFilter(50) >> CtrlValueFilter(127) >> NoteOn(70, 60) >> out3,
        CtrlFilter(43) >> CtrlValueFilter(127) >> SceneSwitch(11),
        CtrlFilter(42) >> CtrlValueFilter(127) >> NoteOn(90, 60) >> out5,

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light8),
        CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light9),
        CtrlFilter(40) >> CtrlValueFilter(127) >> Process(light10),
]


pads2 = [
        #NotesPads HAHAHHAHAHAHHAHAHAHAAA
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
        CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(34, 110) >> SceneSwitch(20),
        CtrlFilter(50) >> CtrlValueFilter(127) >> [NoteOn(54, 60) >> out6, Process(light11)],
        CtrlFilter(42) >> CtrlValueFilter(127) >> [NoteOn(90, 60) >> out7, Process(light12)],

        #lightspad
        CtrlFilter(44) >> CtrlValueFilter(127) >> Process(light1),
        CtrlFilter(45) >> CtrlValueFilter(127) >> Process(light2),
        CtrlFilter(46) >> CtrlValueFilter(127) >> Process(light3),
        CtrlFilter(47) >> CtrlValueFilter(127) >> Process(light4),
        CtrlFilter(48) >> CtrlValueFilter(127) >> Process(light5),
        CtrlFilter(36) >> CtrlValueFilter(127) >> Process(light6),
        CtrlFilter(37) >> CtrlValueFilter(127) >> Process(light7),
        CtrlFilter(38) >> CtrlValueFilter(127) >> Process(light8),
        CtrlFilter(39) >> CtrlValueFilter(127) >> Process(light9),
        CtrlFilter(40) >> CtrlValueFilter(127) >> Process(light10),
]

#ain't no stoping us now
notechanges = [
        KeyFilter('C0') >> Key('G#0'),
        KeyFilter('C#0') >> Key('C0'),
        KeyFilter('D0') >> Key('C0'),
        KeyFilter('D#0') >> Key('D#0'),
        KeyFilter('E0') >> Key('E0'),
        KeyFilter('F0') >> Key('F0'),
        KeyFilter('F#0') >> Key('D#0'),
        KeyFilter('G0') >> Key('F0'),
        KeyFilter('G#0') >> Key('G#0'),
	KeyFilter('A0') >> Key('C1'),
        KeyFilter('A#0') >> Key('A#0'),
	KeyFilter('B0') >> Key('A#0'),
	KeyFilter('C1') >> Key('G#1'),
]

rednotechanges = [
        KeyFilter('C0') >> Key('C0'),
        KeyFilter('C#0') >> Key('C#0'),
        KeyFilter('D0') >> Key('D0'),
        KeyFilter('D#0') >> Key('D#0'),
        KeyFilter('E0') >> Key('E0'),
        KeyFilter('F0') >> Key('F0'),
        KeyFilter('F#0') >> Key('F#0'),
        KeyFilter('G0') >> Key('G0'),
        KeyFilter('G#0') >> Key('G#0'),
        KeyFilter('A0') >> Key('A#0'),
        KeyFilter('A#0') >> Key('B0'),
        KeyFilter('B0') >> Key('C1'),
        KeyFilter('C1') >> Key('D#1'),
]

talkboxdetect = [
	Filter(NOTEON) >> Process(talkbox, True),
	Filter(NOTEOFF) >> Process(talkbox, False),
]


#############################################################################################################
############################################   SETUPS   #####################################################
#############################################################################################################
#############################################################################################################



#encore des lignes de codes incompréhensibles

#hit the road jack
setupsc1 = [

		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),

		Ctrl(3, 5) >> launchkeydaw16,	#ctrl(3 , padmode) 1:drums mode       5 6 7 8: custom		
	#	Ctrl(0, 120) >> out1,
	#	Ctrl(32, 0) >> out1,
		Program(5) >> out1, # 5:rhodes
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(31) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums program 2 du port 128 sur channel 10
]
#billiejean

setupsc2 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
		Program(13) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]
#automatic
setupsc3 = [
		Ctrl(3, 8) >> launchkeydaw16, #pad mode 3 => padmode 5 6 7 8 custom modes
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
		Program(8) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]


#if you feel it
setupsc4 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Program(40) >> out1,
		Program(69) >> out2, #out2 reservé a la talkbox
		Program(105) >> out3, #out3 2em son du clavier
		Program(12) >> out4, #bass
		Program(102) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(111) >> out8,
		Program(128, 10, 3) >> out10, #drums

]


#Gorrillaz
setupsc5 = [
		Ctrl(3, 5) >> launchkeydaw16,			#custom modes : 5:RGB 6:VioletBillieJ 7:rasta 8:disco
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]


#snoop dog
setupsc6 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Program(1) >> out1,
		Program(59) >> out2, #out2 reservé a la talkbox
		Program(59) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(56) >> out8, #2em son du clavier basse
		Program(128, 10, 3) >> out10, #drums

]


#Bad Girls
setupsc7 = [
		Ctrl(3, 8) >> launchkeydaw16,
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(52) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]


#loose yourself to dance
setupsc8 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(103) >> out3, #pad
		Program(8) >> out4, #bass
		Program(112) >> out5, #Pad 50
		Program(90) >> out6, #Pad 43
		Program(99) >> out7, #Pad 42
		Program(105) >> out8, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]



#finaly
setupsc9 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Program(4) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(40) >> out3, #out3 2em son du clavier
		Program(12) >> out4,
		Program(106) >> out5, #Pad 50
		Program(110) >> out6, #Pad 43
		Program(53) >> out8, #Pad 42
		Program(99) >> out7,
		Program(128, 10, 3) >> out10, #drums

]


#the police
setupsc10 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]


#solo clean
setupsc11 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]

#solo satu
setupsc12 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Program(40) >> out1,
		Program(2) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
		Program(128, 10, 3) >> out10, #drums

]


#ain't no stopping us now
setupsc13 = [
                Ctrl(3, 8) >> launchkeydaw16,
                Program(40) >> out1,
                Program(6) >> out2, #out2 reservé a la talkbox
                Program(52) >> out3, #out3 2em son du clavier
                Program(12) >> out4, # bass
                Program(92) >> out5, #Pad 50
                Program(91) >> out6, #Pad 43
                Program(94) >> out7, #Pad 42
                Program(128, 10, 3) >> out10, #drums

]

#diamond real
setupsc14 = [
                Ctrl(3, 8) >> launchkeydaw16,
                Program(2) >> out1,
                Program(6) >> out2, #out2 reservé a la talkbox
                Program(2) >> out3, #out3 2em son du clavier
                Program(12) >> out4, # bass
                Program(100) >> out5, #Pad 50
                Program(107) >> out6, #Pad 43
                Program(112) >> out7, #Pad 42
                Program(128, 10, 3) >> out10, #drums

]

#teckno
setupsc15 = [
                Ctrl(3, 8) >> launchkeydaw16,
                Program(77) >> out1,
                Program(94) >> out2,
                Program(68) >> out3, #out3 2em son du clavier
                Program(12) >> out4, # bass
                Program(69) >> out5, #Pad 50
                Program(91) >> out6, #Pad 43
                Program(94) >> out7, #Pad 42
                Program(128, 10, 3) >> out10, #drums

]

#red hot mary wilson
setupsc16 = [
                Ctrl(3, 8) >> launchkeydaw16,
                Program(2) >> out1,
                Program(77) >> out2,
                Program(68) >> out3, #out3 2em son du clavier
                Program(12) >> out4, # bass
                Program(69) >> out5, #Pad 50
                Program(91) >> out6, #Pad 43
                Program(94) >> out7, #Pad 42
                Program(128, 10, 3) >> out10, #drums

]

talkboxsetup = [
		Program(6) >> out2, #out2 reservé a la talkbox

]

#Get down
setupsc19 = [
		Ctrl(3, 8) >> launchkeydaw16,
		Program(2) >> out1,
		Program(66) >> out2, #out2 reservé a la talkbox
		Program(103) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # bass
		Program(111) >> out5, #Pad 50
		Program(90) >> out6, #Pad 43
		Program(110) >> out7, #Pad 42
		Program(105) >> out8, #pad
		Program(128, 10, 3) >> out10, #drums

]

#ladies night
setupsc20 = [

		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),

		Ctrl(3, 6) >> launchkeydaw16,   #ctrl(3 , padmode) 1:drums mode       5 6 7 8: custom
		Program(3) >> out1, #
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(31) >> out3, #out3 2em son du clavier
		Program(12) >> out4, # 33:acoustic bass
		Program(106) >> out5, #Pad 50
		Program(110) >> out6, #Pad 43
		Program(53) >> out8, #Pad 42
		Program(99) >> out7,
		Program(128, 10, 3) >> out10, #drums program 2 du port 128 sur channel 10
]
##############################################################################
##############################################################################

synthsetup0 = [
		Ctrl(32, 0) >> out1,
		Program(21) >> out1,
]


synthsetup1 = [
		Ctrl(32, 0) >> out1,
		Program(22) >> out1,
]


synthsetup2 = [
		Ctrl(32, 0) >> out1,
		Program(23) >> out1,
]


synthsetup3 = [
		Ctrl(32, 0) >> out1,
		Program(24) >> out1,
]


synthsetup4 = [
		Ctrl(32, 0) >> out1,
		Program(25) >> out1,
]


synthsetup5 = [
		Ctrl(32, 0) >> out1,
		Program(26) >> out1,
]


synthsetup6 = [
		Ctrl(32, 0) >> out1,
		Program(27) >> out1,
]


synthsetup7 = [
		Ctrl(32, 0) >> out1,
		Program(28) >> out1,
]


synthsetup8 = [
		Ctrl(32, 0) >> out1,
		Program(29) >> out1,
]


synthsetup9 = [
		Ctrl(32, 0) >> out1,
		Program(30) >> out1,
]


synthsetup10 = [
		Ctrl(32, 0) >> out1,
		Program(71) >> out1,
]


synthsetup11 = [
		Ctrl(32, 0) >> out1,
		Program(72) >> out1,
]


synthsetup12 = [
		Ctrl(32, 0) >> out1,
		Program(73) >> out1,
]


synthsetup13 = [
		Ctrl(32, 0) >> out1,
		Program(74) >> out1,
]


synthsetup14 = [
		Ctrl(32, 0) >> out1,
		Program(75) >> out1,
]


synthsetup15 = [
		Ctrl(32, 0) >> out1,
		Program(76) >> out1,
]


synthsetup16 = [
		Ctrl(32, 0) >> out1,
		Program(77) >> out1,
]


synthsetup17 = [
		Ctrl(32, 0) >> out1,
		Program(78) >> out1,
]


synthsetup18 = [
		Ctrl(32, 0) >> out1,
		Program(79) >> out1,
]


synthsetup19 = [
		Ctrl(32, 0) >> out1,
		Program(80) >> out1,
]


synthsetup20 = [
		Ctrl(32, 0) >> out1,
		Program(81) >> out1,
]


synthsetup21 = [
		Ctrl(32, 0) >> out1,
		Program(82) >> out1,
]


synthsetup22 = [
		Ctrl(32, 0) >> out1,
		Program(83) >> out1,
]


synthsetup23 = [
		Ctrl(32, 0) >> out1,
		Program(84) >> out1,
]


synthsetup24 = [
		Ctrl(32, 0) >> out1,
		Program(85) >> out1,
]


synthsetup25 = [
		Ctrl(32, 0) >> out1,
		Program(86) >> out1,
]


synthsetup26 = [
		Ctrl(32, 0) >> out1,
		Program(87) >> out1,
]


synthsetup27 = [
		Ctrl(32, 0) >> out1,
		Program(88) >> out1,
]


synthsetup28 = [
		Ctrl(32, 0) >> out1,
		Program(89) >> out1,
]


synthsetup29 = [
		Ctrl(32, 0) >> out1,
		Program(90) >> out1,
]


synthsetup30 = [
		Ctrl(32, 0) >> out1,
		Program(91) >> out1,
]


synthsetup31 = [
		Ctrl(32, 0) >> out1,
		Program(92) >> out1,
]


synthsetup32 = [
		Ctrl(32, 0) >> out1,
		Program(93) >> out1,
]


synthsetup33 = [
		Ctrl(32, 0) >> out1,
		Program(94) >> out1,
]


synthsetup34 = [
		Ctrl(32, 0) >> out1,
		Program(95) >> out1,
]


synthsetup35 = [
		Ctrl(32, 0) >> out1,
		Program(96) >> out1,
]


synthsetup36 = [
		Ctrl(32, 0) >> out1,
		Program(97) >> out1,
]


synthsetup37 = [
		Ctrl(32, 0) >> out1,
		Program(98) >> out1,
]


synthsetup38 = [
		Ctrl(32, 0) >> out1,
		Program(99) >> out1,
]

################################################################################
###############################################################################

pianosetup0 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(1) >> out1, #piano
                #Ctrl(32, 8) >> out2, #bank 8 sur channel 2
                #Program(81) >> out2, #sine wave
#                Ctrl(32, 1) >>out4,
#                Program(34) >> out4, #fingered bass
]

pianosetup1 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(2) >> out1, #piano
		#Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		#Program(81) >> out2, #sine wave
#		Ctrl(32, 1) >>out4,
#		Program(34) >> out4, #fingered bass
]

pianosetup2 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(3) >> out1, #piano
		#Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		#Program(81) >> out2, #sine wave
#		Ctrl(32, 1) >>out4,
#		Program(34) >> out4, #fingered bass
]

pianosetup3 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(4) >> out1, #piano
		#Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		#Program(81) >> out2, #sine wave
#		Ctrl(32, 1) >>out4,
#		Program(34) >> out4, #fingered bass
]

pianosetup4 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(5) >> out1, #piano
#Ctrl(32, 8) >> out2, #bank 8 sur channel 2
#Program(81) >> out2, #sine wave
#		Ctrl(32, 1) >>out4,
#		Program(34) >> out4, #fingered bass
]

#############################################################################################
#############################################################################################


organsetup0 = [
                Ctrl(3, 5) >> launchkeydaw16,
                Ctrl(32, 0) >> out1, #bank 1 sur channel 1
                Program(31) >> out1, 
]


organsetup1 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(32) >> out1,

]

organsetup2 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(33) >> out1,

]

organsetup3 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(34) >> out1,

]

organsetup4 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(35) >> out1,

]


organsetup5 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(36) >> out1,

]

organsetup6 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(37) >> out1,

]

organsetup7 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(38) >> out1,

]

organsetup8 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(39) >> out1,

]

organsetup9 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(40) >> out1,

]

organsetup10 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(41) >> out1,

]

organsetup11 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(42) >> out1,

]

organsetup12 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(43) >> out1,

]



########################################################################################################
########################################################################################################


bassesetup0 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(11) >> out1,
Ctrl(32, 0) >> out4,
Program(11) >> out4,
]

bassesetup1 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(12) >> out1,
Ctrl(32, 0) >> out4,
Program(12) >> out4,
]

bassesetup2 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(13) >> out1,
Ctrl(32, 0) >> out4,
Program(13) >> out4,
]

bassesetup3 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(14) >> out1,
Ctrl(32, 0) >> out4,
Program(14) >> out4,
]

bassesetup4 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(15) >> out1,
Ctrl(32, 0) >> out4,
Program(15) >> out4,
]

bassesetup5 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(16) >> out1,
Ctrl(32, 0) >> out4,
Program(16) >> out4,
]

bassesetup6 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(17) >> out1,
Ctrl(32, 0) >> out4,
Program(17) >> out4,
]

bassesetup7 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(18) >> out1,
Ctrl(32, 0) >> out4,
Program(18) >> out4,
]

bassesetup8 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(19) >> out1,
Ctrl(32, 0) >> out4,
Program(19) >> out4,
]

bassesetup9 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(20) >> out1,
Ctrl(32, 0) >> out4,
Program(20) >> out4,
]

bassesetup10 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(21) >> out1,
Ctrl(32, 0) >> out4,
Program(21) >> out4,
]

bassesetup11 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(22) >> out1,
Ctrl(32, 0) >> out4,
Program(22) >> out4,
]

bassesetup12 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(23) >> out1,
Ctrl(32, 0) >> out4,
Program(23) >> out4,
]

bassesetup13 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(24) >> out1,
Ctrl(32, 0) >> out4,
Program(24) >> out4,
]

bassesetup14 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(25) >> out1,
Ctrl(32, 0) >> out4,
Program(25) >> out4,
]

bassesetup15 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(26) >> out1,
Ctrl(32, 0) >> out4,
Program(26) >> out4,
]

bassesetup16 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(51) >> out1,
Ctrl(32, 0) >> out4,
Program(51) >> out4,
]

bassesetup17 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(52) >> out1,
Ctrl(32, 0) >> out4,
Program(52) >> out4,
]

bassesetup18 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(53) >> out1,
Ctrl(32, 0) >> out4,
Program(53) >> out4,
]

bassesetup19 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(54) >> out1,
Ctrl(32, 0) >> out4,
Program(54) >> out4,
]

bassesetup20 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(55) >> out1,
Ctrl(32, 0) >> out4,
Program(55) >> out4,
]

bassesetup21 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(56) >> out1,
Ctrl(32, 0) >> out4,
Program(56) >> out4,
]
bassesetup22 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(57) >> out1,
Ctrl(32, 0) >> out4,
Program(57) >> out4,
]

bassesetup23 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(58) >> out1,
Ctrl(32, 0) >> out4,
Program(58) >> out4,
]

bassesetup24 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(59) >> out1,
Ctrl(32, 0) >> out4,
Program(59) >> out4,
]

bassesetup25 = [
Ctrl(3, 5) >> launchkeydaw16,
Ctrl(32, 0) >> out1,
Program(60) >> out1,
Ctrl(32, 0) >> out4,
Program(60) >> out4,
]



# out1 clavier principal  out2 clavier principal avec keysplit out3: pads out4:basse out 10 batterie elec

#hit the road jack
scenerun1 =[

	pads1,
	ChannelSplit({
		1: Transpose(-19) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Velocity(curve=2) >> out1,
	#	2: Transpose(5) >> out2,
	#	3: Transpose(5) >> out3,
		4: MakeMonophonic() >> Transpose(5) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> Velocity(fixed=80) >> [out10, send_percu_i2c],

})
]

# billiejean
scenerun2 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C1', Velocity(fixed=40) >> Transpose(5) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> [out2, talkboxdetect], Velocity(fixed=102) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(5) >> [out1, talkboxdetect] ),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(5) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#Automatic
scenerun3 =[
	pads1,
	ChannelSplit({
		1: Velocity(fixed=102) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(5) >> [out1, talkboxdetect],
		4: MakeMonophonic() >> Transpose(5) >> Velocity(fixed=90) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]


# if you feel it
scenerun4 =[
	ifyoufeelpads,
	ChannelSplit({
		1: KeySplit('C3', Velocity(fixed=90) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-40) >> out2, Velocity(fixed=100) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> [out1, talkboxdetect] ),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(8) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]


# feel good inc
scenerun5 =[
	pads1,
	ChannelSplit({
		1: Velocity(fixed=102) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> out1 ,
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(20) >> Velocity(fixed=127) >> out4,
		10: Pass() >> [out10, send_percu_i2c],
})
]

#snoop Dog
scenerun6 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C3', Velocity(fixed=63) >> Transpose(24) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> [out2, talkboxdetect],
			KeySplit('C4', Velocity(fixed=75) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(0) >> out1,
				Velocity(fixed=120) >> MakeMonophonic() >> Transpose(0) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out3)),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: KeySplit('D0', Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(26) >> Velocity(fixed=35) >> out8, MakeMonophonic() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(0) >> Velocity(fixed=127) >> out4),
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#Bad Girls
scenerun7 =[
	pads2,
	ChannelSplit({
		1: KeySplit('C2', Velocity(fixed=45) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(3) >> out3,
			Velocity(fixed=103) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(3) >> [out1, talkboxdetect]),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(3) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#Bad Girls2
scenerun71 =[
        pads1,
        ChannelSplit({
                1: KeySplit('C2', Velocity(fixed=45) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(5) >> out3,
                        Velocity(fixed=103) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(5) >> [out1, talkboxdetect]),
        #       2: Transpose(10) >> out2,
        #       3: Transpose(10) >> out3,
                4: MakeMonophonic() >> Transpose(5) >> Velocity(fixed=127) >> out4,
                10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#loose yourself to dance
scenerun8 =[
	newpadsdf,
	ChannelSplit({
		1: KeySplit('C4', Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(15) >> [out2, talkboxdetect], Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(15) >> out1 ),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(15) >> Velocity(fixed=100) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#finaly
scenerun9 =[
	finalypads,
	ChannelSplit({
		1: KeySplit('F2', Velocity(fixed=50) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(18) >> out8,
			KeySplit('F3', Velocity(fixed=102) >> Transpose(6) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out3,
				 Velocity(fixed=65) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-6) >> out1 )),

		4: MakeMonophonic() >> Transpose(6) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]


#i can't stand loosing you
scenerun10 =[
	padspolice,
	ChannelSplit({
	#	1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect], 
		1: Velocity(fixed=80) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(15) >> out1,
		4: MakeMonophonic() >> Transpose(15) >> Velocity(fixed=127) >> out4,
		10: Pass() >> Velocity(fixed=78) >> [out10, send_percu_i2c],
})
]

#solo guitare1 clean
scenerun11 =[
	pads1,
	ChannelSplit({
	#	1: KeySplit('C3', Velocity(fixed=40) >> Transpose(5) >> [out2, talkboxdetect],
		1: Velocity(fixed=80) >> Transpose(5) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
		4: MakeMonophonic() >> Transpose(17) >> Velocity(fixed=120) >> out4,
		10: Pass() >> KeyFilter(36) >> Velocity(fixed=73) >> [out10, send_percu_i2c],
})
]

#solo satu
scenerun12 =[
	pads1,
	ChannelSplit({
	#	1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect], 
		1: Pass() >> Transpose(0) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
		4: MakeMonophonic() >> Transpose(12) >> Velocity(fixed=120) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]


#ain't no stop
scenerun13 =[
        pads2,
        ChannelSplit({
                1: KeySplit('D2', Velocity(fixed=45) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> out3,
                        Velocity(fixed=103) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> out1),
        #       2: Transpose(10) >> out2,
        #       3: Transpose(10) >> out3,
                4: MakeMonophonic() >> Velocity(fixed=127) >> notechanges >> out4,
                10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]


#diamond real
scenerun14 =[
        padsdreal,
        ChannelSplit({
                1: Pass() >> Transpose(5) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
        #       2: Transpose(10) >> out2,
        #       3: Transpose(10) >> out3,
                4: MakeMonophonic() >> Transpose(17) >> Velocity(fixed=100) >> out4,
                10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#teckno
scenerun15 =[
        pads1,
        ChannelSplit({
                1: KeySplit('G2', Velocity(fixed=70) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-22) >> out5,
                        [Velocity(fixed=25) >> KeyColorFilter('white') >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(2) >> out1, Velocity(fixed=55) >> KeyColorFilter('black') >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(29) >> out2]),
        #       2: Transpose(10) >> out2,
        #       3: Transpose(10) >> out3,
                4: MakeMonophonic() >> Transpose(2) >> Velocity(fixed=100) >> out4,
                10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#redhot
scenerun16 =[
        padsdreal,
        ChannelSplit({
                1: KeySplit('C2', Velocity(curve=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(14) >> out2,
                        Velocity(curve=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-24) >> [out1, talkboxdetect]),
        #       2: Transpose(10) >> out2,
        #       3: Transpose(10) >> out3,
                4: MakeMonophonic() >> rednotechanges >> Velocity(fixed=127) >> out4,
                10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#Get down
scenerun19 =[
	getdownpads,
	ChannelSplit({
		1: KeySplit('C4', Velocity(curve=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-7) >> out1,
			Velocity(fixed=43) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-7) >> [out2, talkboxdetect]),
		4: MakeMonophonic() >> Transpose(5) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> [out10, send_percu_i2c],
})
]

#ladies night
scenerun20 =[
	finalypads,
	ChannelSplit({
		1: Transpose(-16) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Velocity(curve=2) >> Velocity(multiply=0.5) >> out1,
		4: MakeMonophonic() >> Transpose(8) >> Velocity(fixed=127) >> out4,
		10: Pass() >> KeyFilter(36) >> Velocity(fixed=80) >> [out10, send_percu_i2c],

})
]

transposescene0 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(0) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]


transposescene1 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(1) >> out1,
                4: MakeMonophonic() >> Transpose(1) >> out4,
                10: Pass() >> out10,
})
]

transposescene2 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(2) >> out1,
                4: MakeMonophonic() >> Transpose(2) >> out4,
                10: Pass() >> out10,
})
]

transposescene3 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(3) >> out1,
                4: MakeMonophonic() >> Transpose(3) >> out4,
                10: Pass() >> out10,
})
]

transposescene4 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(4) >> out1,
                4: MakeMonophonic() >> Transpose(4) >> out4,
                10: Pass() >> out10,
})
]

transposescene5 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(5) >> out1,
                4: MakeMonophonic() >> Transpose(5) >> out4,
                10: Pass() >> out10,
})
]

transposescene6 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(6) >> out1,
                4: MakeMonophonic() >> Transpose(6) >> out4,
                10: Pass() >> out10,
})
]

transposescene7 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(7) >> out1,
                4: MakeMonophonic() >> Transpose(7) >> out4,
                10: Pass() >> out10,
})
]

transposescene8 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> out1,
                4: MakeMonophonic() >> Transpose(8) >> out4,
                10: Pass() >> out10,
})
]

transposescene9 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(9) >> out1,
                4: MakeMonophonic() >> Transpose(9) >> out4,
                10: Pass() >> out10,
})
]

transposescene10 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(10) >> out1,
                4: MakeMonophonic() >> Transpose(10) >> out4,
                10: Pass() >> out10,
})
]

transposescene11 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(11) >> out1,
                4: MakeMonophonic() >> Transpose(11) >> out4,
                10: Pass() >> out10,
})
]

talkboxrun =[
        pads1,
        ChannelSplit({
                1: Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(24) >> [out2, talkboxdetect],
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]




organrun =[
        pads1,
        ChannelSplit({
                1: Velocity(fixed=90) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]


pianorun =[
        pads1,
        ChannelSplit({
                1: Velocity(gamma=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]



synthrun =[
        pads1,
        ChannelSplit({
                1: Velocity(gamma=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]

bassmoderun =[
        pads1,
        ChannelSplit({
                1: Velocity(fixed=90) >> MakeMonophonic() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]


#scene et program numbers 

scenes = {
	1: Scene("1: hit the road jack", scenerun1, init_patch=setupsc1),
	2: Scene("billiejean", scenerun2, init_patch=setupsc2),
	3: Scene("automatic", scenerun3, init_patch=setupsc3),
	4: Scene("if you feel it", scenerun4, init_patch=setupsc4),
	5: Scene("feel good inc", scenerun5, init_patch=setupsc5),
	6: Scene("the next episode", scenerun6, init_patch=setupsc6),
	7: Scene("bad girls", scenerun7, init_patch=setupsc7),
	8: Scene("loose yourself", scenerun8, init_patch=setupsc8),
	9: Scene("ain't no stop", scenerun9, init_patch=setupsc9),
	10: Scene("can't stand loosin", scenerun10, init_patch=setupsc10),
	11: Scene("soloclean", scenerun11, init_patch=setupsc11),
	12: Scene("solosatu", scenerun12, init_patch=setupsc12),
	13: Scene("ain't no stop", scenerun13, init_patch=setupsc13),
	14: Scene("diamond real", scenerun14, init_patch=setupsc14),
	15: Scene("teckno", scenerun15, init_patch=setupsc15),
	16: Scene("ladies night", scenerun20, init_patch=setupsc20),
	19: Scene("get down", scenerun19, init_patch=setupsc19),
	20:  Scene("bad girls2", scenerun71, init_patch=setupsc7),

	21: Scene("ORGAN", organrun, init_patch=organsetup0),
	22: Scene("PIANO", pianorun, init_patch=pianosetup0),
	23: Scene("E.PIANO", pianorun, init_patch=synthsetup0),
	24: Scene("TALKBOX", talkboxrun, init_patch=talkboxsetup),



	30: Scene("transpose0", transposescene0, init_patch=setupsc12),
	31: Scene("transpose1", transposescene1, init_patch=setupsc12),
	32: Scene("transpose2", transposescene2, init_patch=setupsc12),
	33: Scene("transpose3", transposescene3, init_patch=setupsc12),
	34: Scene("transpose4", transposescene4, init_patch=setupsc12),
	35: Scene("transpose5", transposescene5, init_patch=setupsc12),
	36: Scene("transpose6", transposescene6, init_patch=setupsc12),
	37: Scene("transpose7", transposescene7, init_patch=setupsc12),
	38: Scene("transpose8", transposescene8, init_patch=setupsc12),
	39: Scene("transpose9", transposescene9, init_patch=setupsc12),
	40: Scene("transpose10", transposescene10, init_patch=setupsc12),
	41: Scene("transpose11", transposescene11, init_patch=setupsc12),



	50: Scene("pianomode0", transposescene0, init_patch=pianosetup0),
	51: Scene("pianomode1", transposescene0, init_patch=pianosetup1),
	52: Scene("pianomode2", transposescene0, init_patch=pianosetup2),
	53: Scene("pianomode3", transposescene0, init_patch=pianosetup3),
	54: Scene("pianomode4", transposescene0, init_patch=pianosetup4),

	#3: Scene("a", scenerun3, init_patch=setupsc3),
	#4: Scene("If you feel it", sceneru, init_patch=setupssc4),

	60: Scene("organmode0", organrun, init_patch=organsetup0),
	61: Scene("organmode1", organrun, init_patch=organsetup1),
	62: Scene("organmode2", organrun, init_patch=organsetup2),
	63: Scene("organmode3", organrun, init_patch=organsetup3),
	64: Scene("organmode4", organrun, init_patch=organsetup4),
	65: Scene("organmode5", organrun, init_patch=organsetup5),
	66: Scene("organmode6", organrun, init_patch=organsetup6),
	67: Scene("organmode7", organrun, init_patch=organsetup7),
	68: Scene("organmode8", organrun, init_patch=organsetup8),
	69: Scene("organmode9", organrun, init_patch=organsetup9),
	70: Scene("organmode10", organrun, init_patch=organsetup10),
	71: Scene("organmode11", organrun, init_patch=organsetup11),
	72: Scene("organmode12", organrun, init_patch=organsetup12),


	80: Scene("smode0", scenerun1, init_patch=synthsetup0),
	81: Scene("smode1", scenerun1, init_patch=synthsetup1),
	82: Scene("smode2", scenerun1, init_patch=synthsetup2),
	83: Scene("smode3", scenerun1, init_patch=synthsetup3),
	84: Scene("smode4", scenerun1, init_patch=synthsetup4),
	85: Scene("smode5", scenerun1, init_patch=synthsetup5),
	86: Scene("smode6", scenerun1, init_patch=synthsetup6),
	87: Scene("smode7", scenerun1, init_patch=synthsetup7),
	88: Scene("smode8", scenerun1, init_patch=synthsetup8),
	89: Scene("smode9", scenerun1, init_patch=synthsetup9),
	90: Scene("smode0", scenerun1, init_patch=synthsetup10),
	91: Scene("smode1", scenerun1, init_patch=synthsetup11),
	92: Scene("smode2", scenerun1, init_patch=synthsetup12),
	93: Scene("smode3", scenerun1, init_patch=synthsetup13),
	94: Scene("smode4", scenerun1, init_patch=synthsetup14),
	95: Scene("smode5", scenerun1, init_patch=synthsetup15),
	96: Scene("smode6", scenerun1, init_patch=synthsetup16),
	97: Scene("smode7", scenerun1, init_patch=synthsetup17),
	98: Scene("smode8", scenerun1, init_patch=synthsetup18),
	99: Scene("smode9", synthrun, init_patch=synthsetup19),
	100: Scene("smode0", synthrun, init_patch=synthsetup20),
	101: Scene("smode1", synthrun, init_patch=synthsetup21),
	102: Scene("smode2", synthrun, init_patch=synthsetup22),
	103: Scene("smode3", synthrun, init_patch=synthsetup23),
	104: Scene("smode4", synthrun, init_patch=synthsetup24),
	105: Scene("smode5", synthrun, init_patch=synthsetup25),
	106: Scene("smode6", synthrun, init_patch=synthsetup26),
	107: Scene("smode7", synthrun, init_patch=synthsetup27),
	108: Scene("smode8", synthrun, init_patch=synthsetup28),
	109: Scene("smode9", synthrun, init_patch=synthsetup29),
	110: Scene("smode0", synthrun, init_patch=synthsetup30),
	111: Scene("smode1", synthrun, init_patch=synthsetup31),
	112: Scene("smode2", synthrun, init_patch=synthsetup32),
	113: Scene("smode3", synthrun, init_patch=synthsetup33),
	114: Scene("smode4", synthrun, init_patch=synthsetup34),
	115: Scene("smode5", synthrun, init_patch=synthsetup35),
	116: Scene("smode6", synthrun, init_patch=synthsetup36),
	117: Scene("smode7", synthrun, init_patch=synthsetup37),
	118: Scene("smode8", synthrun, init_patch=synthsetup38),


	120: Scene("bassmode0", bassmoderun, init_patch=bassesetup0),
	121: Scene("bassmode1", bassmoderun, init_patch=bassesetup1),
	122: Scene("bassmode2", bassmoderun, init_patch=bassesetup2),
	123: Scene("bassmode3", bassmoderun, init_patch=bassesetup3),
	124: Scene("bassmode4", bassmoderun, init_patch=bassesetup4),
	125: Scene("bassmode5", bassmoderun, init_patch=bassesetup5),
	126: Scene("bassmode6", bassmoderun, init_patch=bassesetup6),
	127: Scene("bassmode7", bassmoderun, init_patch=bassesetup7),
	128: Scene("bassmode8", bassmoderun, init_patch=bassesetup8),
	129: Scene("bassmode9", bassmoderun, init_patch=bassesetup9),
	130: Scene("bassmode10", bassmoderun, init_patch=bassesetup10),
	131: Scene("bassmode11", bassmoderun, init_patch=bassesetup11),
	132: Scene("bassmode12", bassmoderun, init_patch=bassesetup12),
	133: Scene("bassmode13", bassmoderun, init_patch=bassesetup13),
	134: Scene("bassmode14", bassmoderun, init_patch=bassesetup14),
	135: Scene("bassmode15", bassmoderun, init_patch=bassesetup15),
	136: Scene("bassmode16", bassmoderun, init_patch=bassesetup16),
	137: Scene("bassmode17", bassmoderun, init_patch=bassesetup17),
	138: Scene("bassmode18", bassmoderun, init_patch=bassesetup18),
	139: Scene("bassmode19", bassmoderun, init_patch=bassesetup19),
	140: Scene("bassmode20", bassmoderun, init_patch=bassesetup20),
	141: Scene("bassmode21", bassmoderun, init_patch=bassesetup21),
	142: Scene("bassmode22", bassmoderun, init_patch=bassesetup22),
	143: Scene("bassmode23", bassmoderun, init_patch=bassesetup23),
	144: Scene("bassmode24", bassmoderun, init_patch=bassesetup24),
	145: Scene("bassmode25", bassmoderun, init_patch=bassesetup25),



}


run(
	control = control,
	scenes = scenes,
#	pre=pre,
#	post=post,
	)
