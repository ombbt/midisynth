
from mididings import *
from mididings.event import *
from mididings.extra import *
from mididings.engine import *
from dotenv import *
from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO
import time

load = load_dotenv(dotenv_path='/home/pi/midisynth/examples/variables.env')
#require('dotenv').config({override: true})

TRANSPOSE =int(os.getenv('TRANSPOSE'))

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
print(TRANSPOSE)
scenenumber = 1
pressed = set()
timmer1 = 1.0
timmer2 = 1.0
#tran = 0
#offset = 1
#print(type(tran))
def readkeypad(self):
#	TRANSPOSE =int(os.getenv('TRANSPOSE'))
	#global offset
	#global tran
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
				if keycode == 0:  # scene1
					#initran = 5
					#tran = initran + offset
					#print(type(tran))
					#os.putenv(TRANSPOSE,4)
					#os.environ['TRANSPOSE'] = 2 
					switch_scene(1, subscene=None)
					#print("TRANSPOSE= ", TRANSPOSE, "  initran=", initran, " offset= ", offset )
				elif keycode == 1:
					print("scene 4")
				elif keycode == 2:
					print("scene 7")
				elif keycode == 3:
					print("scene 0")
				elif keycode == 4:	#scene 2
					#initran = -4
					#tran = initran + offset
					# os.environ['TRANSPOSE'] = 4
					switch_scene(2, subscene=None)
					#print("TRANSPOSE=", TRANSPOSE, "   initran= ", initran, " offset= ", offset )
				elif keycode == 5:
					print("scene 5")
				elif keycode == 6:
					print("scene 8")
				elif keycode == 7:
					print("scene F")
				elif keycode == 8: #scene 3
					switch_scene(3, subscene=None)
					
				elif keycode == 9:
					print("scene 6")
				elif keycode == 10:
					print("scene 9")
				elif keycode == 11:
					print("scene E")
				elif keycode == 12:
					print("autodestruction")
					global timmer1
					timmer1 = time.process_time()
					timmer1 = timmer1 +0.09 
					print("timmer1", timmer1)
				elif keycode == 13:
					offset = offset +1
					print("transpose + offset = ", offset)
				elif keycode == 14:
					offset = offset -1
					print("transpose - offset = ", offset)
				elif keycode == 15:
					print("lights on off")

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
				
				#	print("i love coffe")
		GPIO.setup(rows[i], GPIO.IN)


config(
	backend='alsa',
	client_name='mididings',
	in_ports = [	('Launchkey MK3 49 LKMK3 MIDI IN', '16:0'),
			('Arduino Leonardo MIDI 1', '20:0')
			
		],
	out_ports = [
	('Launchkey MK3 49 LKMK3 DAW IN','16:1'),
        ('mididings output','128:0')	],
)

pre= Filter(~CTRL) % Print('input', portnames='in')  // ~Filter(PROGRAM)
#pre = Filter(NOTEON) % Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 

control = [ 
	Process(readkeypad),
	Filter(PROGRAM) >> SceneSwitch(scenenumber)
]
 # SceneSwitch()
	 



  #crée le programe control Filter(PROGRAM) et SceneSwitch() sont des fonction existantes, voir doc mididings
	#	pre = Print('input', portname='in') >> ~Filter(PROGRAM)
#pre = Print()

#definie les sounds/output
out1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
out2 = Output('mididings output', 2)  #channel "2"	
out3 = Output('mididings output', 3) 
out4 = Output('mididings output', 4)
out10 = Output('mididings output', 10) #channel "10"

launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)
launchkeydaw10 = Output('Launchkey MK3 49 LKMK3 DAW IN',10)
launchkeydaw12 = Output('Launchkey MK3 49 LKMK3 DAW IN',12)

#Gestion des lumierres avec les pads
def light1(self):
	print("light1")
def light2(self):
	print("light2")
def light3(self):
	print("light3")
def light4(self):
	print("light4")
def light5(self):
	print("light5")
def light6(self):
	print("light6")
def light7(self):
	print("light7")
def light8(self):
	print("light8")
def light9(self):
	print("light9")
def light10(self):
	print("light10")


pads1 = [
	#NotesPads
	CtrlFilter(51) >> Panic(bypass=True),
	CtrlFilter(50) >> NoteOn(54, 60) >> out3,
	CtrlFilter(42) >> NoteOn(55, 60) >> out3,
	CtrlFilter(43) >> NoteOn(56, 60) >> out3,

	#lightspad
	CtrlFilter(44) >> Process(light1),
	CtrlFilter(45) >> Process(light2),
	CtrlFilter(46) >> Process(light3),
	CtrlFilter(47) >> Process(light4),
	CtrlFilter(48) >> Process(light5),
	CtrlFilter(36) >> Process(light6),
	CtrlFilter(37) >> Process(light7),
	CtrlFilter(38) >> Process(light8),
	CtrlFilter(39) >> Process(light9),
	CtrlFilter(40) >> Process(light10),
#	CtrlFilter(38) >> NoteOff(54, 60) >> spam3,
]


#encore des lignes de codes incompréhensibles

#hit the road jack
setupsc1 = [

		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),

		Ctrl(3, 5) >> launchkeydaw16,	#ctrl(3 , padmode) 1:drums mode       5 6 7 8: custom
	
	#	Ctrl(0, 120) >> out1,
	#	Ctrl(32, 0) >> out1,
		Program(5) >> out1, # 5:rhodes
		Program(1) >> out3,
		Ctrl(32, 1) >> out4,
		Program(33) >> out4, # 33:acoustic bass
		Program(128, 10, 2) >> out10, #drums program 2 du port 128 sur channel 10
]
#billiejean
setupsc2 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Ctrl(32, 8) >> out1, #bank 8 sur channel 1
		Program(17) >> out1, #rock detuned organ sur bank 8
		
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass

]
#automatic
setupsc3 = [
		Ctrl(3, 8) >> launchkeydaw16, #pad mode 3 => padmode 5 6 7 8 custom modes
		Ctrl(32, 8) >> out1,		#bank 8 on ch1
		Program(17) >> out1,
		Ctrl(32, 8) >> out2,
		Program(81) >> out2,

		Ctrl(32, 8) >> out4,
		Program(40) >> out4,  #synth bass channel 8 pg 38

]

# out1 clavier principal  out2 clavier principal avec keysplit out3: pads out4:basse out 10 batterie elec

#hit the road jack
scenerun1 =[

	pads1,
	ChannelSplit({
		1: Transpose(5) >> out1,
	#	2: Transpose(5) >> out2,
	#	3: Transpose(5) >> out3,
		4: MakeMonophonic() >> Transpose(5) >> out4,
		10: Pass() >> out10,

})
]

# billiejean
scenerun2 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> out2, Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(10) >> out1 ),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(-2) >> out4,
		10: Pass() >> out10,
})
]

#Automatic
scenerun3 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C3', Velocity(fixed=40) >> Transpose(19) >> out2, Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(7) >> out1),
		4: MakeMonophonic() >> Transpose(-5) >> out4,
		10: Pass() >> out10,
})
]


#scene et program numbers 

scenes = {
	1: Scene("1: hit the road jack", scenerun1, init_patch=setupsc1),
	2: Scene("billiejean", scenerun2, init_patch=setupsc2),
	3: Scene("automatic", scenerun3, init_patch=setupsc3),
}


run(
	control = control,
	scenes = scenes,
	
#	pre=pre,
#	post=post,
	)
