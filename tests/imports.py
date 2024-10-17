from microbit import *

import log
import machine
import music
import neopixel
import os
import power
import radio
import random
import speech
import utime
from microbit.SoundEvent import SOUND_EVENT_CLAP
from microbit.microphone import was_event

accelerometer.get_gestures()
compass.calibrate()
button_a.is_pressed()
button_b.is_pressed()
pin0.read_analog()
display.scroll('test')
z = temperature()

microbit.panic(5)
utime.sleep(30)
rt = running_time()
display.clear()
display.show(Image.ANGRY)
display.set_pixel()
uart.read(5)
i2c.read(4, 3, True)
last_mic_event = microphone.current_event()
mic_event = microphone.was_event(SOUND_EVENT_CLAP)
os.size()
speaker.on()
spi.read(10)
neopixel.clear()
uart.readall()
music.play(music.BA_DING,pin0)
radio.config(length=5)
speech.say("I am a little robot",  speed=92, pitch=60, throat=190, mouth=190)
log.delete(True)
machine.time_pulse_us(3, 8, 1000)
power.off()
random.randrange(5, 8)

