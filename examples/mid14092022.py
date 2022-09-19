from mididings import *
# from mididings.extra import *

# import fluidsynth
# import time

config(
	backend='alsa',
	client_name='mididings',
	in_ports = [('Launchkey MK3 49 LKMK3 MIDI IN', '20:0')],
	out_ports = [
#	('Launchkey MK3 49 LKMK3 DAW IN','20:1'),
        ('mididings output','128:0')
	],
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


#definie les sounds/output
spam1 = Output('mididings output', 1)  #channel 1 on port 'FLUID synth
spam2 = Output('mididings output', 3)  #channel "3"	

#encore des lignes de codes incompréhensibles
dummy_1 = KeySplit('C3', spam1 ,spam2)
dummy_2 = KeySplit('C2', spam2 ,spam1)

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
