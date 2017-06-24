import os
import platform
import sys
from string import Template

script_dir_path = os.path.dirname(os.path.realpath(__file__))

baud = 115200
image_name = "esp8266-20170612-v1.9.1.bin"
remote_dir_url = "http://micropython.org/resources/firmware/"

def guess_port_identifier():
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
	
	return port

def emulate_invocation(templateString, config):
	command = Template(templateString).substitute(config)
	#print("Emulating '" + command + "'")
	sys.argv=command.split()

def retrieval_config():
	filesystem_lookup = filesystem_config()
	return dict(filesystem_lookup,
		remote_image_url = remote_dir_url + image_name		
	)
	
def filesystem_config():
	return dict(
		local_image_path = script_dir_path + "/flash/firmwares/" + image_name		
	)

def hardware_config():
	return dict(
		baud=baud,
		port=guess_port_identifier()
	)
	
def ampyRelease():
	from ampy import cli
	if cli._board is not None:
		try:
			cli._board.close()
		except:
			pass
	
def putFile(frompath, topath):
	from ampy import pyboard, cli
	try:
		putCommand = "ampy --port ${port} put ${frompath} ${topath}"
		putConfig = hardware_config()
		putConfig.update(
			frompath=frompath,
			topath=topath
		)
		emulate_invocation(putCommand, putConfig)
		try:
			cli.cli()
		except SystemExit:
			pass
		
	except pyboard.PyboardError:
		print("Is cockle unplugged or in use by another program?")
	
	ampyRelease()


def resetBoard():
	from ampy import pyboard, cli
	try:
		print('Resetting Cockle')
		emulate_invocation("ampy --port ${port} reset", hardware_config())
		try:
			cli.cli()
		except SystemExit:
			pass

	except pyboard.PyboardError:
		print("Is cockle unplugged or in use by another program?")
	
	ampyRelease()

