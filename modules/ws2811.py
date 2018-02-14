from neopixel import NeoPixel
from machine import Pin
from color import *

num_pixels = 0
pixels = []

RGB = (0, 1, 2, 3)
GRB = (1, 0, 2, 3)
RBG = (0, 2, 1, 3)
PL9823 = RGB
WS2811 = GRB


def startPixels(pin=None, num=None, order=None):
    global num_pixels, pixels
    if pin is None:
        pin = Pin(4)  # NodeMCUv2 Pin D2
    if num is None:
        num = 8
    if order is not None:
        NeoPixel.ORDER = order
    num_pixels = num
    pixels = NeoPixel(pin, num)


def setPixel(index, color, show=True):
    pixels[index] = color
    if show:
        pixels.write()


def showPixels():
    pixels.write()


def clearPixels(indexes=None, color=black, show=True):
    if indexes == None:
        indexes = range(num_pixels)
    for index in indexes:
        setPixel(index, color, False)
    if show:
        showPixels()

if __name__ == "__main__":
    startPixels()
    clearPixels()