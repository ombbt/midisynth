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


pre = Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 

control =  Filter(PROGRAM) >> SceneSwitch() 

notechanges = [
	KeyFilter('C3') >> Key('E2'),
	KeyFilter('C#3') >> Key('A5'),
	KeyFilter('D3') >> Key('C3'),
	KeyFilter('D#3') >> Key('D3'),
	KeyFilter('E3') >> Key('F4'),
	KeyFilter('F3') >> Key('F1'),
	KeyFilter('F#3') >> Key('F5'),
	KeyFilter('G3') >> Key('F3'),
	KeyFilter('B4') >> Key('A4'),
]

     
#definie les sounds/output
spam1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
spam2 = Output('mididings output', 2)  #channel "2"	
launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)


#encore des lignes de codes incompréhensibles


setupsc1 = [
		Program(97) >> spam1,

		Program(65) >> spam2,

]

setupsc2 = [
		
		Program(95) >> spam1,
		Program(64) >> spam2,

]



dummy_2 =[
	KeySplit('C3', spam2, spam1 >> notechanges),
	
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
