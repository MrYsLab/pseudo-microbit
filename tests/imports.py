from microbit import *
import music
import neopixel
import radio
import speech
import os

panic(5)
sleep(30)
rt = running_time()
display.clear()
display.show(Image.ANGRY)
display.set_pixel()
uart.read(5)
i2c.read(4, 3, True)
compass.calibrate()
button_a.is_pressed()
button_b.is_pressed()
pin0.read_analog()
display.scroll('test')
z = temperature()
os.size()
neopixel.clear()
music.play(music.BA_DING,pin0)
radio.config(length=5)
speech.say("I am a little robot",  speed=92, pitch=60, throat=190, mouth=190)

music.play(music.BA_DING,)
