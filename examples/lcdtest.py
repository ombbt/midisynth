from mididings import *
from mididings.event import *
# from mididings.extra import *

# import fluidsynth
# import time

config(
	backend='alsa',
	client_name='mididings',
	in_ports = [('Launchkey MK3 49 LKMK3 MIDI IN', '20:0')],
	out_ports = [
	('Launchkey MK3 49 LKMK3 DAW IN','20:1'),
        ('mididings output','128:0')	],
)

#hook(
#	AutoRestart(),
#)
pre = Print('input', portnames='in') >> ~Filter(PROGRAM)
post = Print('output', portnames='out') 

control = Filter(PROGRAM) >> SceneSwitch()      
  #crée le programe control Filter(PROGRAM) et SceneSwitch() sont des fonction existantes, voir doc mididings

#definie les sounds/output
spam1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
spam2 = Output('mididings output', 2)  #channel "2"	
launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)

#syslcd pour definir les commande sysex pour l'ecran lcd
sysexlcd1 = '\xF0\x00\x20\x29\x02\x0F\x04\xF7' #set default display
sysexlcd2 = '\xF0\x00\x20\x29\x02\x0F\x04\x00\x54\x65\x73\x74\xF7' #set default dispay + prout
sysexlcd3 = '\xF0\x00\x20\x42\x43\x32\x43\xF7' # ramdom
notecall = NoteOn(98,57)


#encore des lignes de codes incompréhensibles

setupsc1 = [

		NoteOn(12, 127) >> launchkeydaw16, # fout la merde car il envoie sur le port launchkey mais ne reconecte pas le port fluidsynth
#		
		NoteOn(98, 45) >> launchkeydaw3,
		NoteOn(99, 121) >> launchkeydaw3,
		NoteOn(100, 100) >> launchkeydaw3,
		NoteOn(101, 90) >> launchkeydaw2,
#		SysEx(sysexlcd2) >> launchkeydaw16,
		
#		MidiEvent(SysExEvent, launchkeydaw16, sysexlcd),
		Program(97) >> spam1,

		Program(65) >> spam2,

		KeySplit('C3', spam1 ,spam2),  
]

setupsc2 = [
		SysEx(sysexlcd2),
		Program(95) >> spam1,
		Program(64) >> spam2,


]

setupsc3 = [
		SysEx(sysexlcd3),
		Program(96) >> spam1,
		Program(63) >> spam2,

]


dummy_2 =[
	KeySplit('C2', spam2 ,spam1),
	SysEx(sysexlcd2) >> launchkeydaw16,
	
]
def preset1():
	Call(setup_lights)






#scene et program numbers 

scenes = {
	1: Scene("Dummy Scene1", dummy_2, init_patch=setupsc1),
	2: Scene("Dummy Scene2", dummy_2, init_patch=setupsc2),
	3: Scene("Dummy Scene3", dummy_2, init_patch=setupsc3),
}



run(
        control = control,
	scenes = scenes,
#	pre=pre,
#	post=post,
)
