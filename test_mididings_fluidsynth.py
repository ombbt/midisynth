from mididings import *
# from mididings.extra import *

# import fluidsynth
# import time

config(
	backend='alsa',
	client_name='launchkey_transposed_24',
	in_ports = [('Launchkey MK3 49 LKMK3 MIDI IN', '20:0')],
	out_ports = [
#	('Launchkey MK3 49 LKMK3 DAW IN','20:1'),
        ('FLUID Synth (556)','128:0')
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

run(
        Transpose(1),
#	pre=pre,
#	post=post,
)
