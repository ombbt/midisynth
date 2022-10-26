
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
			('Arduino Leonardo MIDI 1', '16:0')
			
		],
	out_ports = [
	('Launchkey MK3 49 LKMK3 DAW IN','20:1'),
        ('mididings output','128:0')	],
)

#hook(
#	AutoRestart(),
#
pre= Filter(~CTRL) % Print('input', portnames='in')  // ~Filter(PROGRAM)
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

pads = [
	CtrlFilter(38) >> NoteOn(54, 60) >> out3,
#	CtrlFilter(38) >> NoteOff(54, 60) >> spam3,
]


#encore des lignes de codes incompréhensibles
#aparrement un dummy serait un patch???? pas sur
setupsc1 = [
#	launchkeydaw16,
		NoteOn(12, 127) >> launchkeydaw16,   #  Channel(16),

		Ctrl(3, 5) >> launchkeydaw16,	#ctrl(3 , padmode) 1:drums mode       5 6 7 8: custom
	
		Ctrl(0, 120) >> out1,
		Ctrl(32, 0) >> out1,
		Program(1) >> out1, # 5:rhodes
		Program(1) >> out3,
		Program(33) >> out4, # 33:acoustic bass
		Program(128, 10, 2) >> out10, #drums program 2 du port 128 sur channel 10

]

setupsc2 = [
		
		Program(95) >> out1,
		Program(64) >> out2,


]

setupsc3 = [
				
		Program(63) >> out2,

]



scenerun1 =[
	
	pads,
	ChannelSplit({
		1: Transpose(5) >> out1,
		2: Transpose(5) >> out2,
		3: Transpose(5) >> out3,
		4: MakeMonophonic() >> Transpose(5) >> out4,
		10: Pass() >> out10,

})

]




#scene et program numbers 

scenes = {
	1: Scene("1: hit the road jack", scenerun1, init_patch=setupsc1),
	2: Scene("Automatic", scenerun1, init_patch=setupsc2),
	3: Scene("billie jean", scenerun1, init_patch=setupsc3),
}



run(
        control = control,
	scenes = scenes,
	pre=pre,
#	post=post,
)
