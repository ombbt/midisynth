from mididings import *
from mididings.event import *
from mididings.extra import *
# from mididings.extra import *

# import fluidsynth
# import time
#pad


config(
	backend='alsa',
	client_name='mididings',
	in_ports = [
		('Arduino Leonardo MIDI 1', '20:0'),
		('Launchkey MK3 49 LKMK3 MIDI IN', '16:0')],
	out_ports = [
	('Launchkey MK3 49 LKMK3 DAW IN','16:1'),
        ('mididings output','128:0')	],
)

#pre= Print('input', portnames='in')  // ~Filter(PROGRAM)
pre = Filter(CTRL) % Print('input', portnames='in') // ~Filter(PROGRAM)
post = Print('output', portnames='out') 



control =  Filter(PROGRAM) >> SceneSwitch() 


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

notespads1 = [
	CtrlFilter(38) >> NoteOn(54, 60) >> spam3,
	CtrlFilter(51) >> Panic(bypass=True),
#	Channel(1) >> CtrlFilter(38) >> NoteOff(54, 60) >> spam3,
]

notespads2 = [
	CtrlFilter(37) >> NoteOn(54, 60) >> spam2,
	CtrlFilter(38) >> Panic(bypass=True),
]



scenespads = [
	CtrlFilter(40) >> SceneSwitch(1),
	CtrlFilter(41) >> SceneSwitch(2),
	CtrlFilter(42) >> SceneSwitch(3),

]

#encore des lignes de codes incompréhensibles
#aparrement un dummy serait un patch???? pas sur
setupsc1 = [
		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),
#		NoteOn(11, 127) >> launchkeydaw16,   #enable touch truc je sais pas quoi merde

		Ctrl(3, 5) >> launchkeydaw16,	#ctrl(3 , padmode) 1:drums mode 5 6 7 8 custom
		
		Program(48) >> spam1,
		Program(24) >> spam3,
		Program(65) >> spam2,
]


setupsc2 = [
		Ctrl(3, 6) >> launchkeydaw16,
		Program(95) >> spam1,
		Program(64) >> spam2,


]


setupsc3 = [
		Ctrl(3, 7) >> launchkeydaw16,
		Program(5) >> spam1,
		Program(63) >> spam2,

]



dummy_1 =[
	notespads1,
	scenespads,
	ChannelSplit({
		1: spam1,
		2: spam2,
})

]


dummy_2 =[
	notespads2,
	scenespads,
	ChannelSplit({
		1: spam1,
		2: spam2,
})
]



dummy_3 =[
	KeySplit('C3', spam1, spam2),
	scenespads,
]


#scene et program numbers 

scenes = {
	1: Scene("Dummy Scene1", dummy_1, init_patch=setupsc1),
	2: Scene("Dummy Scene2", dummy_2, init_patch=setupsc2),
	3: Scene("Dummy Scene3", dummy_3, init_patch=setupsc3),
}

#scenespads = [
#	CtrlFilter(40) >> SceneSwitch(1),
#	CtrlFilter(41) >> SceneSwitch(2),
#	CtrlFilter(42) >> SceneSwitch(3),

#]

run(
        control = control,
	scenes = scenes,
#	pre=pre,
	post=post,
)
