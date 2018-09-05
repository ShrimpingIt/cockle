from cockle import *
from machine import Pin
buttonPins = [pins[num] for num in [1,2,3,4]]
numButtons = len(buttonPins)

for pin in buttonPins:
    pin.init(mode=Pin.IN, pull=Pin.PULL_UP)

def getButtons():
    return [pin.value() for pin in buttonPins]

def getNextButtons(prevButtons):
    while True:
        nextButtons = getButtons()
        if nextButtons != prevButtons:
            return nextButtons

def logButtonChange():
    prevButtons = getButtons()
    while True:
        nextButtons = getNextButtons(prevButtons)
        print(nextButtons)
        prevButtons = nextButtons

def notifyButtonPress(prevButtons = None):
    if prevButtons is None:
        prevButtons = getButtons()
    while True:
        nextButtons = getNextButtons(prevButtons)
        for pos in range(numButtons):
            if nextButtons[pos] == 0 and prevButtons[pos] != 0:
                yield pos
        prevButtons = nextButtons

for pos in notifyButtonPress():
    print(pos)