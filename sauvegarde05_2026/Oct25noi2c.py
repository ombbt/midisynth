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
#display = drivers.Lcd()
#display.lcd_display_string("     bonjour    ", 1)
#display.lcd_display_string("      zen!!     ", 2)

#arduino i2C adresse
#addr = 0x8 # bus address
#bus = SMBus(1) # indicates /dev/ic2-1


config(
	backend='alsa',
	client_name='mididings',
	in_ports = [	('midiarturia', '20:0')	],
	out_ports = [
#	('Launchkey MK3 49 LKMK3 DAW IN','24:1'),
        ('mididings output','128:0')	],
)

#pre= Filter(~CTRL) % Print('input', portnames='in')  // ~Filter(PROGRAM)
pre = Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 

control = [ 
#	Process(readkeypad),
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

potnotesDm = [
CtrlValueFilter(0) >> NoteOff('C5', 0) >> out3,

CtrlValueFilter(1) >> NoteOn('C5', 80) >> out3,

CtrlValueFilter(3) >> NoteOn('C5', 80) >> out3,
CtrlValueFilter(3) >> NoteOff('D5', 0) >> out3,

CtrlValueFilter(4) >> NoteOn('D5', 80) >> out3,
CtrlValueFilter(4) >> NoteOff('C5', 0) >> out3,
CtrlValueFilter(4) >> NoteOff('E5', 0) >> out3,


CtrlValueFilter(5) >> NoteOn('E5', 80) >> out3,
CtrlValueFilter(5) >> NoteOff('D5', 0) >> out3,
CtrlValueFilter(5) >> NoteOff('F5', 0) >> out3,


CtrlValueFilter(6) >> NoteOn('F5', 80) >> out3,
CtrlValueFilter(6) >> NoteOff('E5', 0) >> out3,

CtrlValueFilter(8) >> NoteOn('F5', 80) >> out3,
CtrlValueFilter(8) >> NoteOff('G5', 0) >> out3,

CtrlValueFilter(9) >> NoteOn('G5', 80) >> out3,
CtrlValueFilter(9) >> NoteOff('F5', 0) >> out3,
CtrlValueFilter(9) >> NoteOff('A5', 0) >> out3,

CtrlValueFilter(10) >> NoteOn('A5', 80) >> out3,
CtrlValueFilter(10) >> NoteOff('G5', 0) >> out3,
CtrlValueFilter(10) >> NoteOff('A#5', 0) >> out3,

CtrlValueFilter(11) >> NoteOn('A#5', 80) >> out3,
CtrlValueFilter(11) >> NoteOff('A5', 0) >> out3,
CtrlValueFilter(11) >> NoteOff('C6', 0) >> out3,

CtrlValueFilter(12) >> NoteOn('C6', 80) >> out3,
CtrlValueFilter(12) >> NoteOff('A#5', 0) >> out3,

CtrlValueFilter(12) >> NoteOn('C6', 80) >> out3,
CtrlValueFilter(12) >> NoteOff('D6', 0) >> out3,

CtrlValueFilter(13) >> NoteOn('D6', 80) >> out3,
CtrlValueFilter(13) >> NoteOff('C6', 0) >> out3,

CtrlValueFilter(16) >> NoteOn('D6', 80) >> out3,
CtrlValueFilter(16) >> NoteOff('C6', 0) >> out3,

CtrlValueFilter(19) >> NoteOn('D6', 80) >> out3,
CtrlValueFilter(19) >> NoteOff('E6', 0) >> out3,

CtrlValueFilter(20) >> NoteOn('E6', 80) >> out3,
CtrlValueFilter(20) >> NoteOff('D6', 0) >> out3,
CtrlValueFilter(20) >> NoteOff('F6', 0) >> out3,

CtrlValueFilter(21) >> NoteOn('F6', 80) >> out3,
CtrlValueFilter(21) >> NoteOff('E6', 0) >> out3,

CtrlValueFilter(24) >> NoteOn('F6', 80) >> out3,
CtrlValueFilter(24) >> NoteOff('G6', 0) >> out3,


CtrlValueFilter(25) >> NoteOn('G6', 80) >> out3,
CtrlValueFilter(25) >> NoteOff('F6', 0) >> out3,
CtrlValueFilter(25) >> NoteOff('A6', 0) >> out3,

CtrlValueFilter(26) >> NoteOn('A6', 80) >> out3,
CtrlValueFilter(26) >> NoteOff('G6', 0) >> out3,

CtrlValueFilter(29) >> NoteOn('A6', 80) >> out3,

CtrlValueFilter(30) >> NoteOff('A6', 0) >> out3,

]

potnotes = [
CtrlValueFilter(0) >> NoteOff('G3', 0) >> out3,

CtrlValueFilter(1) >> NoteOn('G3', 80) >> out3,
CtrlValueFilter(1) >> NoteOff('A4', 0) >> out3,


CtrlValueFilter(2) >> NoteOn('A4', 80) >> out3,
CtrlValueFilter(2) >> NoteOff('G3', 0) >> out3,
CtrlValueFilter(2) >> NoteOff('B4', 0) >> out3,


CtrlValueFilter(3) >> NoteOn('B4', 80) >> out3,
CtrlValueFilter(3) >> NoteOff('A4', 0) >> out3,
CtrlValueFilter(3) >> NoteOff('C5', 0) >> out3,

CtrlValueFilter(4) >> NoteOn('C5', 80) >> out3,
CtrlValueFilter(4) >> NoteOff('B4', 0) >> out3,
CtrlValueFilter(4) >> NoteOff('D5', 0) >> out3,


CtrlValueFilter(5) >> NoteOn('D5', 80) >> out3,
CtrlValueFilter(5) >> NoteOff('C5', 0) >> out3,
CtrlValueFilter(5) >> NoteOff('E5', 0) >> out3,


CtrlValueFilter(6) >> NoteOn('E5', 80) >> out3,
CtrlValueFilter(6) >> NoteOff('D5', 0) >> out3,
CtrlValueFilter(6) >> NoteOff('F5', 0) >> out3,


CtrlValueFilter(7) >> NoteOn('F5', 80) >> out3,
CtrlValueFilter(7) >> NoteOff('E5', 0) >> out3,
CtrlValueFilter(7) >> NoteOff('G5', 0) >> out3,


CtrlValueFilter(8) >> NoteOn('G5', 80) >> out3,
CtrlValueFilter(8) >> NoteOff('F5', 0) >> out3,
CtrlValueFilter(8) >> NoteOff('A5', 0) >> out3,

CtrlValueFilter(9) >> NoteOn('A5', 80) >> out3,
CtrlValueFilter(9) >> NoteOff('G5', 0) >> out3,
CtrlValueFilter(9) >> NoteOff('B5', 0) >> out3,

CtrlValueFilter(10) >> NoteOn('B5', 80) >> out3,
CtrlValueFilter(10) >> NoteOff('A5', 0) >> out3,
CtrlValueFilter(10) >> NoteOff('C6', 0) >> out3,

CtrlValueFilter(11) >> NoteOn('C6', 80) >> out3,
CtrlValueFilter(11) >> NoteOff('B5', 0) >> out3,
CtrlValueFilter(11) >> NoteOff('D6', 0) >> out3,

CtrlValueFilter(12) >> NoteOn('D6', 80) >> out3,
CtrlValueFilter(12) >> NoteOff('C6', 0) >> out3,
CtrlValueFilter(12) >> NoteOff('E6', 0) >> out3,

CtrlValueFilter(13) >> NoteOn('E6', 80) >> out3,
CtrlValueFilter(13) >> NoteOff('D6', 0) >> out3,
CtrlValueFilter(13) >> NoteOff('F6', 0) >> out3,

CtrlValueFilter(14) >> NoteOn('F6', 80) >> out3,
CtrlValueFilter(14) >> NoteOff('E6', 0) >> out3,
CtrlValueFilter(14) >> NoteOff('G6', 0) >> out3,

CtrlValueFilter(15) >> NoteOn('G6', 80) >> out3,
CtrlValueFilter(15) >> NoteOff('F6', 0) >> out3,

CtrlValueFilter(16) >> NoteOff('G6', 0) >> out3,
]


def hittheroadi2c(self):
	display.lcd_display_string("hit the road jack  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x01)

def billiejeani2c(self):
	display.lcd_display_string("   billie jean  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x01)

def automatici2c(self):
	display.lcd_display_string("     automatic  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x02)

def ifyoufeeliti2c(self):
	display.lcd_display_string("  if you feel it  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x03)

def snoopdogi2c(self):
	display.lcd_display_string("  next episode  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x04)

def badgirlsi2c(self):
	display.lcd_display_string("  bad girls  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x05)

def daftpunki2c(self):
	display.lcd_display_string("loose yourself dance", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x06)

def solocleani2c(self):
	display.lcd_display_string("   solo clean  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x07)

def techno1i2c(self):
	display.lcd_display_string("     techno1    ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x0B)

def getdowni2c(self):
	display.lcd_display_string("    get down    ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x09)

def ladiesnighti2c(self):
	display.lcd_display_string("  ladies night   ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x08)

def bemyladyi2c(self):
	display.lcd_display_string("  be my lady   ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x0A)

def technohousei2c(self):
	display.lcd_display_string(" technohouse  ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x0C)

def technoinfectedi2c(self):
	display.lcd_display_string("  infected tech   ", 1)
	display.lcd_display_string("m:1  tr:9", 2)
	bus.write_byte(addr, 0x0D)

#def techno1i2c(self):
#display.lcd_display_string("     techno1    ", 1)
#display.lcd_display_string("m:1  tr:9", 2)
#bus.write_byte(addr, 0x03)
#############################################################################################################
############################################   SETUPS   #####################################################
#############################################################################################################
#############################################################################################################


#encore des lignes de codes incompréhensibles

#hit the road jack
setupsc1 = [



	#	Ctrl(0, 120) >> out1,
	#	Ctrl(32, 0) >> out1,
		Program(5) >> out1, # 5:rhodes
		Program(59) >> out3,
#		Process(hittheroadi2c),
]
#billiejean

setupsc2 = [
		Program(40) >> out1,
		Program(70) >> out3, #out3 2em son du clavier
#		Process(billiejeani2c),
]
#automatic
setupsc3 = [

		Program(40) >> out1,
		Program(70) >> out3, #out3 2em son du clavier
#		Process(automatici2c),

]


#if you feel it
setupsc4 = [
		Program(40) >> out1,
		Program(69) >> out2, #out2 reservé a la talkbox
		Program(105) >> out3, #out3 2em son du clavier
#		Process(ifyoufeeliti2c),
]



#snoop dog
setupsc6 = [
		Program(1) >> out1,
		Program(59) >> out2,
		Program(59) >> out3, #out3 2em son du clavier
		Program(92) >> out5, #Pad 50
		Program(91) >> out6, #Pad 43
		Program(94) >> out7, #Pad 42
#		Process(snoopdogi2c),
]


#Bad Girls
setupsc7 = [
		Program(40) >> out1,
		Program(6) >> out2,
		Program(59) >> out3,
#		Process(badgirlsi2c),

]


#loose yourself to dance
setupsc8 = [
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(59) >> out3, #pot
#		Process(daftpunki2c),
]


#solo clean
setupsc11 = [
		Program(40) >> out1,
		Program(6) >> out2, #out2 reservé a la talkbox
		Program(70) >> out3, #out3 2em son du clavier
#		Process(solocleani2c),
]


#techno
setupsc15 = [
                Program(68) >> out1, #77
                Program(94) >> out2,
                Program(77) >> out3, #out3 2em son du clavier
#		Process(techno1i2c),
]


#get down
setupsc19 = [
		Program(2) >> out1,
		Program(66) >> out2, #out2 reservé a la talkbox
		Program(103) >> out3, #out3 2em son du clavier
#		Process(getdowni2c),
]

#ladies night
setupsc20 = [
		Program(3) >> out1, #out2 reservé a la talkbox
		Program(31) >> out3, #out3 2em son du clavier
#		Process(ladiesnighti2c),
]

#be my lady
setupsc21 = [
		Program(40) >> out1, #out2 reservé a la talkbox
		Program(31) >> out3, #out3 2em son du clavier
#		Process(bemyladyi2c),
]

#technohouse
setupsc22 = [
		Program(5) >> out1, #out2 reservé a la talkbox
		Program(59) >> out3, #out3 2em son du clavier
#		Process(technohousei2c),
]

#technoinfected
setupsc23 = [
		Program(68) >> out1,
		Program(45) >> out2,
		Program(31) >> out3, #out3 2em son du clavier
#		Process(technoinfectedi2c),
]

#sweet disorder
#setupsc24 = [
#Program(35) >> out1,
#Program(45) >> out2,
#Program(31) >> out3, #out3 2em son du clavier
#Process(technoinfectedi2c),
#]
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
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(1) >> out1, #piano
]

pianosetup1 = [
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(2) >> out1, #piano
]

pianosetup2 = [
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(3) >> out1, #piano
]

pianosetup3 = [
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(4) >> out1, #piano
]

pianosetup4 = [
		Ctrl(32, 0) >> out1, #bank 0 sur channel 1
		Program(5) >> out1, #piano
]

#############################################################################################
#############################################################################################


organsetup0 = [
                Ctrl(32, 0) >> out1, #bank 1 sur channel 1
                Program(31) >> out1, 
]


organsetup1 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(32) >> out1,

]

organsetup2 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(33) >> out1,

]

organsetup3 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(34) >> out1,

]

organsetup4 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(35) >> out1,

]


organsetup5 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(36) >> out1,

]

organsetup6 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(37) >> out1,

]

organsetup7 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(38) >> out1,

]

organsetup8 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(39) >> out1,

]

organsetup9 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(40) >> out1,

]

organsetup10 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(41) >> out1,

]

organsetup11 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(42) >> out1,

]

organsetup12 = [
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(43) >> out1,

]



########################################################################################################
########################################################################################################


#hit the road jack
scenerun1 =[
		CtrlFilter(77) >> potnotesDm,
		CtrlFilter(74) >> SceneSwitch(),
		Transpose(-19) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Velocity(curve=2)>> Velocity(multiply=0.6) >> out1,

]

# billiejean
scenerun2 =[
		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=40) >> Transpose(-7) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out2,
]

#Automatic
scenerun3 =[

		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=102) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-7) >> out1,

]


# if you feel it
scenerun4 =[
		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=90) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-52) >> out2,
]


# feel good inc
scenerun5 =[
		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=102) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> out1 ,
]

#snoop Dog
scenerun6 =[
		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=63) >> Transpose(12) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out2,

]

#Bad Girls
scenerun7 =[
		CtrlFilter(77) >> potnotesDm,
		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=103) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(3) >> out1,
]


#loose yourself to dance
scenerun8 =[
		CtrlFilter(74) >> SceneSwitch(),
		Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(1) >> out2,
]

#teckno
scenerun15 =[
	CtrlFilter(77) >> potnotesDm,
	CtrlFilter(74) >> SceneSwitch(),
	KeySplit('G2', Velocity(fixed=70) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-22) >> out1, [Velocity(fixed=25) >> KeyColorFilter('white') >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(2) >> out3, Velocity(fixed=55) >> KeyColorFilter('black') >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(29) >> out2]),

]
#Get down
scenerun19 =[
	CtrlFilter(77) >> potnotesDm,
	CtrlFilter(74) >> SceneSwitch(),
	Velocity(fixed=43) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(-7) >> out2,
]

#ladies night
scenerun20 =[
	CtrlFilter(74) >> SceneSwitch(),
	Transpose(-6) >> Filter(~CTRL) >> Velocity(curve=2) >> Velocity(multiply=0.5) >> out1,
]

#be my lady
scenerun21 =[
	CtrlFilter(74) >> SceneSwitch(),
	Transpose(-1) >> Filter(~CTRL) >> Velocity(fixed=103) >> out1,
]

#technohouse
scenerun22 =[
		CtrlFilter(77) >> potnotesDm,
		CtrlFilter(74) >> SceneSwitch(), 
		Transpose(-6) >> Filter(~CTRL) >> Velocity(curve=2) >> Velocity(multiply=0.6) >> out1,
]

#techno infected
scenerun23 =[
	CtrlFilter(77) >> potnotesDm,
	CtrlFilter(74) >> SceneSwitch(), 
	KeySplit('E3', Transpose(-24) >> Filter(~CTRL) >> Velocity(curve=2) >> Velocity(multiply=0.8) >> out1, Velocity(fixed=75) >> Transpose(-24) >> Filter(~CTRL) >> out2),

]

#sweet disorder
#scenerun24 =[
#	CtrlFilter(77) >> potnotesDm, CtrlFilter(74) >> SceneSwitch(),
#	Transpose(-7) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Velocity(curve=2) >> out1,
#]

transposescene0 = [
	CtrlFilter(74) >> SceneSwitch(),
	Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(0) >> out1,
]


transposescene1 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                11: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(1) >> out1,
                4: MakeMonophonic() >> Transpose(1) >> out4,
                10: Pass() >> out10,
})
]

transposescene2 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                11: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(2) >> out1,
                4: MakeMonophonic() >> Transpose(2) >> out4,
                10: Pass() >> out10,
})
]

transposescene3 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                11: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(3) >> out1,
                4: MakeMonophonic() >> Transpose(3) >> out4,
                10: Pass() >> out10,
})
]

transposescene4 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                11: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(4) >> out1,
                4: MakeMonophonic() >> Transpose(4) >> out4,
                10: Pass() >> out10,
})
]

transposescene5 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(5) >> out1,
                4: MakeMonophonic() >> Transpose(5) >> out4,
                10: Pass() >> out10,
})
]

transposescene6 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(6) >> out1,
                4: MakeMonophonic() >> Transpose(6) >> out4,
                10: Pass() >> out10,
})
]

transposescene7 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(7) >> out1,
                4: MakeMonophonic() >> Transpose(7) >> out4,
                10: Pass() >> out10,
})
]

transposescene8 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(8) >> out1,
                4: MakeMonophonic() >> Transpose(8) >> out4,
                10: Pass() >> out10,
})
]

transposescene9 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(9) >> out1,
                4: MakeMonophonic() >> Transpose(9) >> out4,
                10: Pass() >> out10,
})
]

transposescene10 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(10) >> out1,
                4: MakeMonophonic() >> Transpose(10) >> out4,
                10: Pass() >> out10,
})
]

transposescene11 =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                12: Pass() >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(11) >> out1,
                4: MakeMonophonic() >> Transpose(11) >> out4,
                10: Pass() >> out10,
})
]

organrun =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
                12: Velocity(fixed=90) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]


pianorun =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
                12: Velocity(gamma=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]



synthrun =[
	CtrlFilter(74) >> SceneSwitch(),
        ChannelSplit({
                12: Velocity(gamma=2) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> out1,
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
	5: Scene("the next episode", scenerun6, init_patch=setupsc6),
	6: Scene("bad girls", scenerun7, init_patch=setupsc7),
	7: Scene("loose yourself", scenerun8, init_patch=setupsc8),
	8: Scene("soloclean", scenerun1, init_patch=setupsc11),
	9: Scene("ladies night", scenerun20, init_patch=setupsc20),
	10: Scene("get down", scenerun19, init_patch=setupsc19),
	11: Scene("be my lady", scenerun15, init_patch=setupsc15),
	12: Scene("teckno1", scenerun21, init_patch=setupsc21),
	13: Scene("teckno", scenerun22, init_patch=setupsc22),
	14: Scene("teckno", scenerun23, init_patch=setupsc23),
	21: Scene("ORGAN", organrun, init_patch=organsetup0),
	22: Scene("PIANO", pianorun, init_patch=pianosetup0),
	23: Scene("E.PIANO", pianorun, init_patch=synthsetup0),
#	24: Scene("sweet disorder", scenerun24, init_patch=setupsc24),


	30: Scene("transpose0", transposescene0, init_patch=setupsc1),
	31: Scene("transpose1", transposescene1, init_patch=setupsc1),
	32: Scene("transpose2", transposescene2, init_patch=setupsc1),
	33: Scene("transpose3", transposescene3, init_patch=setupsc1),
	34: Scene("transpose4", transposescene4, init_patch=setupsc1),
	35: Scene("transpose5", transposescene5, init_patch=setupsc1),
	36: Scene("transpose6", transposescene6, init_patch=setupsc1),
	37: Scene("transpose7", transposescene7, init_patch=setupsc1),
	38: Scene("transpose8", transposescene8, init_patch=setupsc1),
	39: Scene("transpose9", transposescene9, init_patch=setupsc1),
	40: Scene("transpose10", transposescene10, init_patch=setupsc1),
	41: Scene("transpose11", transposescene11, init_patch=setupsc1),



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

}


run(
	control = control,
	scenes = scenes,
#	pre=pre,
#	post=post,
	)
