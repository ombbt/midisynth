#!/bin/bash

(STOP=$((SECONDS+5))
until [[ $SECONDS -ge $STOP || $(ps -C fluidsynth -o stat=) =~ S ]]; do :; done &&
aconnect 16:0 128:0 &)
fluidsynth -o synth.midi-bank-select=xg -a alsa -g 1 /home/pi/DecembreSF.sf2
