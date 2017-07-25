from neopixel import NeoPixel
from machine import Pin

num_pixels = 0
pixels = []


def hue_to_rgb(h):
    return hsb_to_rgb(h, 1.0, 1.0)


def hsb_to_rgb(h, s, b):
    if s == 0.0: return b, b, b
    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = b * (1.0 - s)
    q = b * (1.0 - s * f)
    t = b * (1.0 - s * (1.0 - f))
    if i % 6 == 0: rgb = b, t, p
    if i == 1: rgb = q, b, p
    if i == 2: rgb = p, b, t
    if i == 3: rgb = p, q, b
    if i == 4: rgb = t, p, b
    if i == 5: rgb = b, p, q
    return [int(color * 255) for color in rgb]


red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

yellow = [255, 255, 0]
purple = [255, 0, 255]
teal = [0, 255, 255]

orange = [255, 128, 0]
pink = [255, 64, 64]

white = [255, 255, 255]
black = [0, 0, 0]

RGB = (0, 1, 2, 3)
GRB = (1, 0, 2, 3)
PL9823 = RGB
WS2811 = GRB


def startPixels(pin, num, order=None):
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


def clearPixels(indexes=None, show=True, color=black):
    if indexes == None:
        indexes = range(num_pixels)
    for index in indexes:
        setPixel(index, color, False)
    if show:
        showPixels()

if __name__ == "__main__":
    startPixels()
    clearPixels()
