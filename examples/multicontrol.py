from mididings import *
from mididings.event import *
from mididings.extra import *
# from mididings.extra import *

# import fluidsynth
# import time

config(
	backend='alsa',
	client_name='mididings',
	in_ports = [	('Launchkey MK3 49 LKMK3 MIDI IN', '20:0'),
			('MK-425C USB MIDI Keyboard MIDI', '24:0')
			
		],
	out_ports = [
	('Launchkey MK3 49 LKMK3 DAW IN','20:1'),
        ('mididings output','128:0')	],
)

#hook(
#	AutoRestart(),
#
pre= Print('input', portnames='in')  // ~Filter(PROGRAM)
#pre = Filter(NOTEON) % Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 
#    fs = fluidsynth.Synth(),
#    fs.start('alsa'),
#    sfid = fs.sfload("/usr/share/sounds/sf2/FluidR3_GM.sf2"),



control =  Filter(PROGRAM) >> SceneSwitch() 


  #crée le programe control Filter(PROGRAM) et SceneSwitch() sont des fonction existantes, voir doc mididings
	#	pre = Print('input', portname='in') >> ~Filter(PROGRAM)
#pre = Print()

#definie les sounds/output
spam1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
spam2 = Output('mididings output', 2)  #channel "2"	
spam3 = Output('mididings output', 3) 
spam10 = Output('mididings output', 10) #channel "10"

launchkeydaw16 = Output('Launchkey MK3 49 LKMK3 DAW IN', 16)
launchkeydaw1 = Output('Launchkey MK3 49 LKMK3 DAW IN', 1)
launchkeydaw2 = Output('Launchkey MK3 49 LKMK3 DAW IN', 2)
launchkeydaw3 = Output('Launchkey MK3 49 LKMK3 DAW IN', 3)
launchkeydaw10 = Output('Launchkey MK3 49 LKMK3 DAW IN',10)
launchkeydaw12 = Output('Launchkey MK3 49 LKMK3 DAW IN', 12)

pads = [
	CtrlFilter(38) >> NoteOn(54, 60) >> spam3,
#	CtrlFilter(38) >> NoteOff(54, 60) >> spam3,
]


#encore des lignes de codes incompréhensibles
#aparrement un dummy serait un patch???? pas sur
setupsc1 = [
#	launchkeydaw16,
		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),
#		NoteOn(11, 127) >> launchkeydaw16,   #enable touch truc je sais pas quoi merde
		Ctrl(3, 5) >> launchkeydaw16,	#ctrl(3 , padmode) 1:drums mode       5 6 7 8: custom
		
		Program(48) >> spam1,
		Program(24) >> spam3,
		Program(65) >> spam2,

]

setupsc2 = [
		
		Program(95) >> spam1,
		Program(64) >> spam2,


]

setupsc3 = [
		
		
		Program(63) >> spam2,

]



dummy_2 =[
	
	pads,
	ChannelSplit({
		1: Transpose(5) >> spam1,
		2: Transpose(4) >> spam2,

})

#	pads,
]




#scene et program numbers 

scenes = {
	1: Scene("Dummy Scene1", dummy_2, init_patch=setupsc1),
	2: Scene("Dummy Scene2", dummy_2, init_patch=setupsc2),
	3: Scene("Dummy Scene3", dummy_2, init_patch=setupsc3),
}



run(
        control = control,
	scenes = scenes,
	pre=pre,
#	post=post,
)
