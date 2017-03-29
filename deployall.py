#!/usr/bin/python
from six.moves import input

from flash.retrieve import run as flashRetrieve 
from flash.deploy import run as flashDeploy 
from modules.deploy import run as modulesDeploy
from replserver.deploy import run as replserverDeploy 

flashRetrieve()
flashDeploy()
input('Micropython uploaded. Press Cockle reset button, then press Enter')
modulesDeploy()
replserverDeploy()
config.putFile("./regimes/04_rainbow/main.py", "main.py")
input('All modules, boot and main files deployed. Press Cockle reset button, then press Enter')
