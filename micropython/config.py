import os
import platform
import sys
from string import Template

def emulateInvocation(templateString):
	sys.argv=(
		Template(templateString)
			.substitute(globals())
			.split()
	)

baud = 115200
port = None

ostype = platform.system()
if ostype=='Linux':
	port = "/dev/ttyUSB0"
elif ostype=='Darwin':
	port = "/dev/tty.SLAB_USBtoUART"
	
if port == None:
	sys.exit("Couldn't identify operating system and guess serial port location")
elif not os.path.exists(port):
	sys.exit("Serial port not present as expected, is it plugged in? Are drivers installed?")

image_name = "esp8266-20161110-v1.8.6.bin"

script_dir_path = os.path.dirname(os.path.realpath(__file__))
local_image_path = script_dir_path + "/firmwares/" + image_name

remote_dir_url = "http://micropython.org/resources/firmware/"
remote_image_url = remote_dir_url + image_name
