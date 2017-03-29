import sys,os
from string import Template
from ampy import pyboard, cli

import config

script_dir_path = os.path.dirname(os.path.realpath(__file__))

bootPath = 'boot.py'
zippedPath = 'webrepl-inlined.html.gz'

config.putFile(script_dir_path + os.path.sep + bootPath, bootPath)
config.putFile(script_dir_path + os.path.sep + zippedPath, zippedPath)
config.resetBoard()
