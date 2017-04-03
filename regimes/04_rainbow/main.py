from time import sleep
from cockle import pins
from ws2811 import *

num_pixels = 8
allIndexes = range(num_pixels)
startPixels(pins[2], num_pixels)

clearPixels()

# values controlling rainbow
hueChange=0.02
hueSeparation=1.0/8.0
changeDelay=0.02
darkFactor=1/8.0

#hue of first pixel
hueOffset = 0

def darken(rgb, proportion=0.05):
	return [int(value * proportion) for value in rgb]

def rainbow():
    colors = [hue_to_rgb(((i * hueSeparation) + hueOffset) % 1) for i in allIndexes]
    for i in allIndexes:
        setPixel(i, darken(colors[i], darkFactor), False)
    showPixels()

def progression():
    global hueOffset
    while True:
        rainbow()
        sleep(changeDelay)
        hueOffset = hueOffset + hueChange
