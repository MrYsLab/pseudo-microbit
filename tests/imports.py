from microbit import *
import music
import neopixel
import radio
import speech
import os

# some random calls within microbit
uart.read(5)
i2c.read(4, 3, True)
compass.calibrate()
button_a.is_pressed()
pin0.read_analog()
display.scroll(Image.ANGRY)
temperature()

os.size()
neopixel.clear()
music.play(music.BA_DING, False, True)
radio.config(length=5)
speech.say("I am a little robot",  speed=92, pitch=60, throat=190, mouth=190)

