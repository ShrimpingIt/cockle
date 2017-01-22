from time import sleep
from cockle import pins
from ws2811 import *

num_pixels = 8
startPixels(pins[2], num_pixels)
clearPixels()

hueOffset = 0
allIndexes = range(num_pixels)
hueSeparation = 1 / num_pixels
hueChange = hueSeparation
changeDelay = 1

def darken(rgb, proportion=0.05):
	return [int(value * proportion) for value in rgb]

def rainbow():
    global hueOffset
    while True:
        colors = [hue_to_rgb(((i * hueSeparation) + hueOffset) % 1) for i in allIndexes]
        for i in allIndexes:
            setPixel(i, colors[i], False)
        showPixels()
        sleep(changeDelay)
        hueOffset = hueOffset + hueChange
