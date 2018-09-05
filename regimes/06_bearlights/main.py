from cockle import pins
from ws2811 import *
startPixels(pin=pins[2], num=3, order=PL9823)

from scanplayer import ScanPlayer
player = ScanPlayer(busy_pin=pins[6])
list(player.tracks.keys())
player.finishAll(0)
