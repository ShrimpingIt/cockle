import sys,os
from string import Template
from ampy import pyboard, cli
import config

script_dir_path = os.path.dirname(os.path.realpath(__file__))

def upload(moduleNames=('cockle', 'ws2811')):
	print('Uploading Modules')
	for moduleName in moduleNames:
		moduleBaseName = moduleName + ".py"
		config.putFile(script_dir_path + os.path.sep + moduleBaseName, moduleBaseName)

def run():
	upload()

if __name__ == "__main__":
	run()
