import sys,os
from string import Template
from ampy import pyboard, cli

import config

def upload_server_files():
	script_dir_path = os.path.dirname(os.path.realpath(__file__))

	bootPath = 'boot.py'
	zippedPath = 'webrepl-inlined.html.gz'

	config.putFile(script_dir_path + os.path.sep + bootPath, bootPath)
	config.putFile(script_dir_path + os.path.sep + zippedPath, zippedPath)
	config.resetBoard()

def run():
	upload_server_files()
				
if __name__ == "__main__":
	run()
