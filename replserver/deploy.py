import sys
from string import Template
from ampy import pyboard, cli

try:
	port = "/dev/ttyUSB0"

	mainPath = 'main.py'
	zippedPath = 'webrepl-inlined.html.gz'

	putTemplate = Template("ampy --port ${port} put ${frompath} ${topath}")


	try:
		print('Uploading the gzipped webrepl')
		sys.argv = putTemplate.substitute(
			port=port,
			frompath=zippedPath,
			topath=zippedPath
		).split()
		cli.cli()
	except SystemExit:
		pass

	try:
		print('Uploading main.py implementing minimal webserver')
		sys.argv = putTemplate.substitute(
			port=port,
			frompath=mainPath,
			topath=mainPath
		).split()
		cli.cli()
	except SystemExit:
		pass

except ampy.pyboard.PyboardError:
	print("Is " + port + " in use?")
