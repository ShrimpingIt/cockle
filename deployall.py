#!/usr/bin/python
#mainPath = "./regimes/04_rainbow/main.py"
mainPath = None

from time import sleep
from six.moves import input

from config import putFile, resetBoard

from flash.retrieve import run as flashRetrieve
from flash.deploy import run as flashDeploy
from modules.deploy import run as modulesDeploy
from replserver.deploy import run as replserverDeploy


def runFlash():

    print("Checking Micropython image retrieved")
    flashRetrieve()

    print("Deploying Micropython image")
    flashDeploy()

    sleep(4)


def runInstall():

    print("Deploying Modules")
    modulesDeploy()

    print("Deploying REPLServer")
    replserverDeploy()

    if mainPath is not None:
        print("Deploying Application main.py file")
        putFile(mainPath, "main.py")


def run():
    runFlash()
    runInstall()
    print('All modules, replserver boot and application main files deployed. Now unplug the cockle to ensure it resets \a\a\a')


if __name__ == "__main__":
    run()