from time import sleep
from cockle import pins
from ws2811 import *
num_pixels = 8
startPixels(pins[2], num_pixels)
showPixels()

allIndexes = range(num_pixels)
hueSeparation = 1 / num_pixels
hueChange = hueSeparation
hueOffset = 0
changeDelay = 1

def rainbow():
    global hueOffset
    while True:
        colors = [hue(((i * hueSeparation) + hueOffset) % 1) for i in allIndexes]
        for i in allIndexes:
            setPixel(i, colors[i])
        sleep(changeDelay)
        hueOffset = hueOffset + hueChange
