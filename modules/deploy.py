import sys
from string import Template
from ampy import pyboard, cli

try:
	port = "/dev/ttyUSB0"

	moduleNames = ['cockle', 'ws2811']

	putTemplate = Template("ampy --port ${port} put ${frompath} ${topath}")
	resetTemplate = Template("ampy --port ${port} reset")

	for moduleName in moduleNames:
		moduleBaseName = moduleName + ".py"
		try:
			print('Uploading ' + moduleBaseName + "...")
			sys.argv = putTemplate.substitute(
				port=port,
				frompath=moduleBaseName,
				topath=moduleBaseName
			).split()
			cli.cli()
		except SystemExit:
			pass

	try:
		print('Resetting Cockle')
		sys.argv = resetTemplate.substitute(
			port=port
		).split()
		cli.cli()
	except SystemExit:
		pass

except pyboard.PyboardError:
	print("Is " + port + "unplugged or already in use?")
