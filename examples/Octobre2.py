
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

pressed = set()
timmer1 = 1.0
timmer2 = 1.0
offset = 0
mode = False
lightonoff = False
def transposescene():
	global offset
	if offset == 0:
		switch_scene(30, subscene=None)
		print("transpose scene 0")
	elif offset == 1:
		switch_scene(31, subscene=None)
		print("t1")
	elif offset == 2:
		switch_scene(32, subscene=None)
		print("t2")
	elif offset == 3:
		switch_scene(33, subscene=None)
		print("t3")
	elif offset == 4:
		switch_scene(34, subscene=None)
		print("t4")
	elif offset == 5:
		switch_scene(35, subscene=None)
		print("t5")
	elif offset == 6:
		switch_scene(36, subscene=None)
		print("t6")
	elif offset == 7:
		switch_scene(37, subscene=None)
		print("t7")
	elif offset == 8:
		switch_scene(38, subscene=None)
		print("t8")
	elif offset == 9:
		switch_scene(39, subscene=None)
		print("t9")
	elif offset == 10:
		switch_scene(40, subscene=None)
		print("t10")
	elif offset == 11:
		switch_scene(41, subscene=None)
		print("t11")


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
						#os.putenv(TRANSPOSE,4)
						#os.environ['TRANSPOSE'] = 2
						switch_scene(1, subscene=None)
						#print("TRANSPOSE= ", TRANSPOSE, "  initran=", initran, " offset= ", offset )
					elif mode == True:
						print('scene 13')
						switch_scene(13, subscene=None)
				elif keycode == 1:
					if mode == False:
						switch_scene(4, subscene=None)
						print("scene 4")
					elif mode == True:
						print("scene 16")
						#switch_scene(16, subscene=None)
					#switch_scene(4, subscene=None)
				elif keycode == 2:
					if mode == False:
						print("scene 7")
						switch_scene(7, subscene=None)
					elif mode == True:
						print("scene 19 ")
						#switch_scene(19, subscene=None)
				elif keycode == 3:
					if mode == False:
						print("scene 0")
						switch_scene(10, subscene=None)
					elif mode == True:
						print("scene0 mode 2 Electric piano")
						switch_scene(22, subscene=None)
				elif keycode == 4:	#scene 2
					if mode == False:
						switch_scene(2, subscene=None)
					elif mode == True:
						print("scene 14")
						#switch_scene(, subscene=None)
				elif keycode == 5:
					if mode == False:
						#print("scene 5")
						switch_scene(5, subscene=None)
					elif mode == True:
						print("scene 17")
						#switch_scene(, subscene=None)
				elif keycode == 6:
					if mode == False:
						print("scene 8")
						switch_scene(8, subscene=None)
					elif mode == True:
						print("scene 20")
						#switch_scene(, subscene=None)
				elif keycode == 7:
					if mode == False:
						print("scene F")
						switch_scene(11, subscene=None)
					elif mode == True:
						switch_scene(23, subscene=None)
						print("scene F mode 2 YAMAHA GRANPIANO")
				elif keycode == 8: #scene 3
					if mode == False:
						switch_scene(3, subscene=None)
					elif mode == True:
						print("scene15")
						#switch_scene(, subscene=None)
				elif keycode == 9:
					if mode == False:
						print("scene 6")
						switch_scene(6, subscene=None)
					elif mode == True:
						print("scene 18")
						#switch_scene(, subscene=None)
				elif keycode == 10:
					if mode == False:
						print("scene 9")
						switch_scene(9, subscene=None)
					elif mode == True:
						print("scene 21 ORGAN")
						switch_scene(21, subscene=None)
				elif keycode == 11:
					if mode == False:
						print("scene E")
						switch_scene(12, subscene=None)
					elif mode == True:
						print("scene E mode2, Full Talkbox")
						switch_scene(24, subscene=None)
				elif keycode == 12:
					print("autodestruction")
					global timmer1
					timmer1 = time.process_time()
					timmer1 = timmer1 +0.09 
					print("timmer1", timmer1)
				elif keycode == 13:
					if mode == False:
						if lightonoff == False:
							lightonoff = True
							print("light On")
						elif lightonoff == True:
							lightonoff = False
							print("light Off")
					elif mode == True:
						if offset < 11:
							offset = offset +1
							transposescene()
				elif keycode == 14: 
					if mode == False:
						print("eating banana")
					elif mode == True:
						if offset > 0:
							offset = offset -1
							transposescene()

				elif keycode == 15:
					if mode ==False:
						mode = True
						print("switch to mode 2")
					elif mode == True:
						mode = False
						print("switch to mode 1")
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
out1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
out2 = Output('mididings output', 2)  #channel "2"	
out3 = Output('mididings output', 3)
out5 = Output('mididings output', 5)  
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

def talkbox(self, togle):
	if togle == True:
		print("talkboxlight ON")
		print("talkboxMic Activate")
	elif togle == False:
		print("talkboxlight OFF")
		print("talkboxMic Unactivate")

pads1 = [
	#NotesPads HAHAHHAHAHAHHAHAHAHAAA
#	CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
#	CtrlFilter(50) >> CtrlValueFilter(127) >> NoteOn(70, 60) >> out3, 
#	CtrlFilter(43) >> CtrlValueFilter(127) >> NoteOn(80, 60) >> out3,
	CtrlFilter(42) >> CtrlValueFilter(127) >> NoteOn(90, 60) >> out3,

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
#       CtrlFilter(51) >> CtrlValueFilter(127) >> Panic(bypass=True),
#       CtrlFilter(50) >> CtrlValueFilter(127) >> NoteOn(70, 60) >> out3,
        CtrlFilter(43) >> CtrlValueFilter(127) >> SceneSwitch(11),
        CtrlFilter(42) >> CtrlValueFilter(127) >> NoteOn(90, 60) >> out3,

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




talkboxdetect = [
	Filter(NOTEON) >> Process(talkbox, True),
	Filter(NOTEOFF) >> Process(talkbox, False),
]

#encore des lignes de codes incompréhensibles

#hit the road jack
setupsc1 = [

		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),

		Ctrl(3, 5) >> launchkeydaw16,	#ctrl(3 , padmode) 1:drums mode       5 6 7 8: custom		
	#	Ctrl(0, 120) >> out1,
	#	Ctrl(32, 0) >> out1,
		Program(5) >> out1, # 5:rhodes
		Program(119) >> out3,
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


#if you feel it
setupsc4 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Ctrl(32, 8) >> out1, #bank 8 sur channel 1
		Program(17) >> out1, #rock detuned organ sur bank 8
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass

]


#Gorrillaz
setupsc5 = [
		Ctrl(3, 5) >> launchkeydaw16,			#custom modes : 5:RGB 6:VioletBillieJ 7:rasta 8:disco
		Ctrl(32, 8) >> out1, #bank 8 sur channel 1
		Program(17) >> out1, #rock detuned organ sur bank 8
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]


#snoop dog
setupsc6 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Ctrl(32, 0) >> out1, #bank 1 sur channel 1
		Program(5) >> out1, #E. piano RHODES
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
		Ctrl(32, 8) >> out5,
		Program(81) >> out5, #sine wave
]


#Bad Girls
setupsc7 = [
		Ctrl(3, 8) >> launchkeydaw16,
		Ctrl(32, 1) >> out1,
		Program(1) >> out1,
		Program(119) >> out3,
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(63) >> out2, #ssynth brass
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]


#loose yourself to dance
setupsc8 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Ctrl(32, 8) >> out1, #bank 8 sur channel 1
		Program(17) >> out1, #rock detuned organ sur bank 8
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]



#ain't no stop
setupsc9 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Ctrl(32, 8) >> out1, #bank 8 sur channel 1
		Program(17) >> out1, #rock detuned organ sur bank 8
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]


#the police
setupsc10 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Ctrl(32, 8) >> out1, #bank 8 sur channel 1
		Program(17) >> out1, #rock detuned organ sur bank 8
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]


#solo clean
setupsc11 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Ctrl(32, 8) >> out1,
		Program(17) >> out1,
		
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]

#solo satu
setupsc12 = [
		Ctrl(3, 5) >> launchkeydaw16,
		Ctrl(32, 1) >> out1, #bank 1 sur channel 1
		Program(1) >> out1, #piano
		Ctrl(32, 8) >> out2, #bank 8 sur channel 2
		Program(81) >> out2, #sine wave
		Ctrl(32, 1) >>out4,
		Program(34) >> out4, #fingered bass
]

talkboxsetup = [
               #Ctrl(3, 5) >> launchkeydaw16,
                #Ctrl(32, 8) >> out1, #bank 1 sur channel 1
                #Program(1) >> out1, #piano
                Ctrl(32, 8) >> out2, #bank 8 sur channel 2
                Program(81) >> out2, #sine wave
                Ctrl(32, 1) >>out4,
                Program(34) >> out4, #fingered bass
]

epianosetup = [
                #Ctrl(3, 5) >> launchkeydaw16,
                Ctrl(32, 0) >> out1, #bank 0 sur channel 1
                Program(5) >> out1, #piano
                Ctrl(32, 8) >> out2, #bank 8 sur channel 2
                Program(81) >> out2, #sine wave
                Ctrl(32, 1) >>out4,
                Program(34) >> out4, #fingered bass
]

pianosetup = [
                Ctrl(3, 5) >> launchkeydaw16,
                Ctrl(32, 0) >> out1, #bank 0 sur channel 1
                Program(1) >> out1, #piano
                #Ctrl(32, 8) >> out2, #bank 8 sur channel 2
                #Program(81) >> out2, #sine wave
                Ctrl(32, 1) >>out4,
                Program(34) >> out4, #fingered bass
]

organsetup = [
                Ctrl(3, 5) >> launchkeydaw16,
                Ctrl(32, 8) >> out1, #bank 1 sur channel 1
                Program(17) >> out1, 
                #Ctrl(32, 8) >> out2, #bank 8 sur channel 2
                #Program(81) >> out2, #sine wave
                Ctrl(32, 1) >>out4,
                Program(34) >> out4, #fingered bass
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
		1: KeySplit('C3', Velocity(fixed=40) >> Transpose(10) >> [out2, talkboxdetect], Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(10) >> out1 ),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(10) >> out4,
		10: Pass() >> out10,
})
]

#Automatic
scenerun3 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C2', Velocity(fixed=40) >> Transpose(19) >>[out2, talkboxdetect], Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(7) >> out1),
		4: MakeMonophonic() >> Transpose(7) >> out4,
		10: Pass() >> out10,
})
]


# if you feel it
scenerun4 =[
	pads1,
	ChannelSplit({
		1: Velocity(fixed=40) >> Transpose(1) >> out1 ,
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(1) >> out4,
		10: Pass() >> out10,
})
]


# feel good inc
scenerun5 =[
	pads1,
	ChannelSplit({
		1: Velocity(fixed=40) >> Transpose(10) >> out1 ,
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(10) >> out4,
		10: Pass() >> out10,
})
]

#snoop Dog
scenerun6 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C3', Velocity(fixed=40) >> Transpose(24) >> [out2, talkboxdetect],
			KeySplit('C4', Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(0) >> out1,
				Velocity(fixed=40) >> MakeMonophonic() >> Transpose(12) >> PitchbendRange(8192, 8191, in_min=-16382, in_max=16382) >> out5)),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(0) >> out4,
		10: Pass() >> out10,
})
]

#Bad Girls
scenerun7 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C4', Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(10) >> out1,
			Velocity(fixed=40) >> MakeMonophonic() >> Transpose(10) >> out2),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(10) >> out4,
		10: Pass() >> out10,
})
]

#loose yourself to dance
scenerun8 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C4', Velocity(fixed=40) >> Transpose(10) >> [out2, talkboxdetect], Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(10) >> out1 ),
	#	2: Transpose(10) >> out2,
	#	3: Transpose(10) >> out3,
		4: MakeMonophonic() >> Transpose(10) >> out4,
		10: Pass() >> out10,
})
]

#ain't no stop
scenerun9 =[
	pads1,
	ChannelSplit({
		1: KeySplit('C3', Velocity(fixed=40) >> Transpose(24) >> [out2, talkboxdetect], Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(12) >> out1 ),
		4: MakeMonophonic() >> Transpose(0) >> out4,
		10: Pass() >> out10,
})
]


#i can't stand loosing you
scenerun10 =[
	padspolice,
	ChannelSplit({
	#	1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect], 
		1: Velocity(fixed=40) >> Filter(~PITCHBEND) >> Filter(~CTRL) >> Transpose(3) >> out1,
		4: MakeMonophonic() >> Transpose(3) >> out4,
		10: Pass() >> out10,
})
]

#solo guitare1 clean
scenerun11 =[
#	pads2,
	ChannelSplit({
	#	1: KeySplit('C3', Velocity(fixed=40) >> Transpose(5) >> [out2, talkboxdetect],
		1: Velocity(fixed=40) >> Transpose(5) >> out1,
		4: MakeMonophonic() >> Transpose(5) >> out4,
		10: Pass() >> out10,
})
]

#solo satu
scenerun12 =[
	pads1,
	ChannelSplit({
	#	1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect], 
		1: Pass() >> Transpose(0) >> out1,
		4: MakeMonophonic() >> Transpose(0) >> out4,
		10: Pass() >> out10,
})
]


transposescene0 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(0) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]


transposescene1 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(1) >> out1,
                4: MakeMonophonic() >> Transpose(1) >> out4,
                10: Pass() >> out10,
})
]

transposescene2 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(2) >> out1,
                4: MakeMonophonic() >> Transpose(2) >> out4,
                10: Pass() >> out10,
})
]

transposescene3 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(3) >> out1,
                4: MakeMonophonic() >> Transpose(3) >> out4,
                10: Pass() >> out10,
})
]

transposescene4 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(4) >> out1,
                4: MakeMonophonic() >> Transpose(4) >> out4,
                10: Pass() >> out10,
})
]

transposescene5 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(5) >> out1,
                4: MakeMonophonic() >> Transpose(5) >> out4,
                10: Pass() >> out10,
})
]

transposescene6 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(6) >> out1,
                4: MakeMonophonic() >> Transpose(6) >> out4,
                10: Pass() >> out10,
})
]

transposescene7 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(7) >> out1,
                4: MakeMonophonic() >> Transpose(7) >> out4,
                10: Pass() >> out10,
})
]

transposescene8 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(8) >> out1,
                4: MakeMonophonic() >> Transpose(8) >> out4,
                10: Pass() >> out10,
})
]

transposescene9 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(9) >> out1,
                4: MakeMonophonic() >> Transpose(9) >> out4,
                10: Pass() >> out10,
})
]

transposescene10 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(10) >> out1,
                4: MakeMonophonic() >> Transpose(10) >> out4,
                10: Pass() >> out10,
})
]

transposescene11 =[
        pads1,
        ChannelSplit({
        #       1: KeySplit('C3', Velocity(fixed=40) >> Transpose(22) >> [out2, talkboxdetect],
                1: Pass() >> Transpose(11) >> out1,
                4: MakeMonophonic() >> Transpose(11) >> out4,
                10: Pass() >> out10,
})
]



#ain't no stop
talkboxrun =[
        pads1,
        ChannelSplit({
                1: Velocity(fixed=40) >> Transpose(24) >> [out2, talkboxdetect],
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]



#ain't no stop
organrun =[
        pads1,
        ChannelSplit({
                1: Velocity(fixed=40) >> out1,
                4: MakeMonophonic() >> Transpose(0) >> out4,
                10: Pass() >> out10,
})
]


pianorun =[
        pads1,
        ChannelSplit({
                1: Velocity(gamma=2) >> out1,
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

	21: Scene("ORGAN", organrun, init_patch=organsetup),
	22: Scene("PIANO", pianorun, init_patch=pianosetup),
	23: Scene("E.PIANO", pianorun, init_patch=epianosetup),
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
	#3: Scene("a", scenerun3, init_patch=setupsc3),
	#4: Scene("If you feel it", sceneru, init_patch=setupssc4),
}


run(
	control = control,
	scenes = scenes,
	
#	pre=pre,
#	post=post,
	)
