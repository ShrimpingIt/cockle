#!/usr/bin/python
mainPath = "./regimes/04_rainbow/main.py"

from six.moves import input

from config import putFile

from flash.retrieve import run as flashRetrieve 
from flash.deploy import run as flashDeploy 
from modules.deploy import run as modulesDeploy
from replserver.deploy import run as replserverDeploy 

print("Retrieving latest flash image")
flashRetrieve()

print("Deploying flash image")
flashDeploy()

input('Micropython uploaded. Press Cockle reset button, then press Enter')

print("Deploying Modules")
modulesDeploy()

print("Deploying REPLServer")
replserverDeploy()

print("Deploying Application main.py file")
putFile(mainPath, "main.py")

input('All modules, replserver boot and application main files deployed. Press Cockle reset button, then press Enter')
