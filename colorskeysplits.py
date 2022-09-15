from mididings import *
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
# pre = Print('input', portnames='in') >> ~Filter(PROGRAM)
# post = Print('output', portnames='out') 
#    fs = fluidsynth.Synth(),
#    fs.start('alsa'),
#    sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2"),



control = Filter(PROGRAM) >> SceneSwitch()      
  #crée le programe control Filter(PROGRAM) et SceneSwitch() sont des fonction existantes, voir doc mididings
	#	pre = Print('input', portname='in') >> ~Filter(PROGRAM)
#pre = Print()

#definie les sounds/output
spam1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
spam2 = Output('mididings output', 2)  #channel "2"	
launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)


#encore des lignes de codes incompréhensibles
#aparrement un dummy serait un patch???? pas sur
dummy_1 = [
#	launchkeydaw16,
#		NoteOn(12, 0) >> launchkeydaw16,   #  Channel(16),
#	launchkeydaw2,
#		NoteOn(98, 45) >> launchkeydaw2,


#	KeySplit('C3', spam1 ,spam2) >> Channel(1) ,Channel(2),

		NoteOn(12, 127) >> launchkeydaw16, # fout la merde car il envoie sur le port launchkey mais ne reconecte pas le port fluidsynth
		NoteOn(97, 24) >> launchkeydaw2,
		NoteOn(98, 45) >> launchkeydaw3,
		NoteOn(99, 121) >> launchkeydaw3,
		NoteOn(100, 100) >> launchkeydaw3,
		NoteOn(101, 90) >> launchkeydaw2,
		Program(97) >> spam1,

		Program(65) >> spam2,

		KeySplit('C3', spam1 ,spam2) 
]

#def colors():
#	launchkeydaw16
#	NoteOn(12, 127) >> Channel(16),
#	NoteOn(96, 9) >> Channel(1),
#	NoteOn(97, 12) >> Channel(2),




dummy_2 = KeySplit('C2', spam2 ,spam1)



#def preset1():
#	dummy_1
#	colors()







#scene et program numbers 

scenes = {
	1: Scene("Dummy Scene1", dummy_1),
	
	2: Scene("Dummy Scene2", dummy_2),
}



run(
        control = control,
	scenes = scenes,
#	pre=pre,
#	post=post,
)
