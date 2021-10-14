#https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)

#!/bin/bash
say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrols "http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&q=$*&tl=en"; }
#say $*
say " Welcome to the Raspberry Pi Study Helper. For your study session, we will be following the Pomodoro Technique." 
say "That means I will be guiding you to study in sessions of 25 minutes, with a 5 to 10 minute break in between."
say "After every 4 sessions, you will have a longer 15 to 30 minute break. Are you ready to start the first session."