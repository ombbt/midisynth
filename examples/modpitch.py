from mididings import *
from mididings.event import *
from mididings.extra import *
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
#le but du programme est d'envoyer le pitchbend et la modulation uniquement sur une seule channel
#on poura ensuite utiliser la fonction channel() pour envoyer les mod pitch sur le channel de notre choix

modpitch = [ 
	Filter(CTRL),
	Filter(PITCHBEND),
]

pre = Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 

control =  Filter(PROGRAM) >> SceneSwitch() 

     
#definie les sounds/output
spam1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
spam2 = Output('mididings output', 2)  #channel "2"	
launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)


#encore des lignes de codes incompréhensibles


setupsc1 = [
		Program(1) >> spam1,

		Program(65) >> spam2,

]

setupsc2 = [
		
		Program(95) >> spam1,
		Program(64) >> spam2,

]



dummy_2 =[
#	KeySplit('C3', spam2 >> ~Filter(CTRL), spam1), ca ce marche
#	KeySplit('C3', spam2 >> ~ modpitch, spam1),     #	ca non
	KeySplit('C3', spam2 >> ~Filter(CTRL) >> ~Filter(PITCHBEND), spam1),
]




#scene et program numbers 

scenes = {
	1: Scene("Dummy Scene1", dummy_2, init_patch=setupsc1),
	2: Scene("Dummy Scene2", dummy_2, init_patch=setupsc2),
	
}



run(
        control = control,
	scenes = scenes,
	pre=pre,
	post=post,
)
