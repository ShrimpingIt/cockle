# Cockle Tutorial

Get an updated version of this document at [http://shrimping.it/project/cockle/tutorial.pdf](http://shrimping.it/project/cockle/tutorial.pdf) . Text collaboratively maintained by @ShrimpingIt on github [here](https://github.com/ShrimpingIt/cockle/blob/master/tutorial/md)

## Equipment Provided

In your packs you should have...

* A Cockle (NodeMCU v2 board pre-installed with Micropython, our libraries and startup scripts)
* An 8-pixel WS2811 RGB LED display
* A USB A-to-MicroB cable
* A 3-way jumper cable with 2.54mm pitch female sockets

## Preparing your Cockle

@ShrimpingIt pre-configures NodeMCUv2 boards with Micropython, with a set of useful libraries and a startup script corresponding to the project they were distributed with, turning them into a _Cockle_. If you have a brand-new cockle, this step has already been completed for you.

However, if you are configuring your own NodeMCUv2 as a Cockle or you want to wipe and reinstall your Cockle with the latest build, follow the steps in _Appendix A_ below.

## Connecting the LED Display

* You will need...
	* The 8-pixel Display
	* The Jumper wires

Look on the back of your LED display. It should have three pins going into it, and three pins going out. Find the end of the board with the following three connections.

* Data In - labelled DIN
* Power - labelled 5V or 4-7VDC
* Ground - labelled GND

Use the jumper wires to attach to the Cockle as follows
* DIN -->D2
* 4-7VDC --> Vin
* GND --> GND

## Connecting to the Cockle via Wifi

* You will need...
	* The Orange USB cable
	* The Cockle

* Step 1: Plug in the Cockle to give it power
	* The cockle's USB Micro-B socket can be fragile. Be careful when plugging and unplugging the cable. If the cable doesn't slide in easily, try turning the plug upside down

* Step 2: Connect to the newly available wifi access point
	* Wifi networks have a name or ESSID. Normally your laptop takes a few minutes to refresh the list of available network ESSIDs in menus. Turning on and off your laptop's wifi can accelerate this.
	* The Cockle appears with an ESSID containing a unique number like Micropython-34fe57
	* The default Wifi password is ```micropythoN``` with a capital N as the last letter

* Step 3: Load the console in the browser
	* Wait for a bit
	* Connect your browser to http://192.168.4.1
	* When the page appears click on Connect
	* Type the password ```shrimping``` when challenged

## Connecting to the Cockle via Serial

A more technical way to connect uses a 'serial' or 'UART' connection over the USB wire. 

The Cockle uses a CP2102 UART module, [drivers here](http://shrimping.it/drivers/cp2102/) and the default connection speed (baud rate) is 115200. For example on a linux machine you can connect like...

* Type ```screen /dev/ttyUSB0 115200``` and press ```Return```
* When the terminal goes blank, press ```Return``` a second time

If the Cockle has connected successfully, you should see three chevrons like this...

    >>>

...and you can continue to the next step ```Issuing Commands```

###### Troubleshooting

* If the console has gone blank, but the chevrons don't appear try the following until they do
	* try pressing the ```CTRL+C``` keys together to try and kill any sequence of steps which was already running. This should return you to the chevrons.
	* visit Appendix A: Configuring your Cockle, to reset your Cockle to 'factory' configuration

## Issuing commands

After connecting, we should be in what is known as a REPL - a Read, Eval, Print Loop.

This means that the Cockle is...

* ***READING*** the commands we send
* ***EVALUATING*** the commands (running them, often generating a result)
* ***PRINTING*** the result (showing the result on screen)
* ***LOOPING*** back (returning to the READING step - over and over again)

Let's try it out to learn some fundamental programming concepts.

### Core Programming Concepts
* Values
    * Type ```4+4``` and press ```Return```. What happens? That was an arithmetic expression, which results in a number.
    * Type ```4*4``` with an asterisk instead and press ```Return```. (hint ```x``` is treated as a letter in a computer language).
    * Enter ```'Hello' + 'World'```
* Names
    * Enter ```square = 4*4```
    * Enter ```square``` (we just assigned a value to a name, so we can refer to it later)
    * Enter ```capital = 'Paris'```
    * Enter ```capital```
* Steps
    * Enter ```raw_input('What is the capital of Colombia? ')```
    * Enter ```capital = raw_input('What is the capital of Colombia? ')```
* Groups of Values: Lists, Dictionaries
    * Enter ```sequence = [3,4,5,6,7,8]```
    * Enter ```sequence```
    * Enter ```sequence[0]```
    * Enter ```sequence[1:4]```
    * Enter ```[num*num for num in sequence]```
* Groups of Steps: Blocks and Functions
    * Enter ```range(2,6)```
    * Enter ```def square(x):```
    * Press Tab, then Enter ```return x*x```
    * Delete all spaces/tabs then press ```Return```
    * Enter ```square(4)```

### Colors, Lists and Loops

* Lists
	* Enter ```yellow = [255,255,0]```
	* Enter ```yellow``` and it should show your list
	* Enter ```red```  this should show a list which was previously defined
	* Enter ```setPixel(0,red)```
	* Enter ```setPixel(1,green)```
	* Enter ```setPixel(2,blue)```

##### Libraries

Libraries contain reference implementations of functions for example ```sqrt(4*4)``` in the python ```math``` library calculates square roots.

Type the following two lines

```
from math import sqrt
sqrt(4*4)
```

## Appendix A: Configuring your own NodeMCU

* Install **python3** on your laptop. 
	- Our config scripts run in _python3_ **and** _python2_. However, _micropython_ is a dialect of _python3_. Our advice; learn one language version
* Install **pip3** on your laptop
* Install **pyserial**, **adafruit-ampy** and **esptool** using *pip3*. For example, linux and mac users would run commands in the console as follows...
```
sudo pip3 install pyserial
sudo pip3 install adafruit-ampy
sudo pip3 install esptool
```
* Get our scripts from the cockle repository ...
	- ...download a [snapshot of our scripts](https://github.com/ShrimpingIt/cockle/archive/master.zip)
	OR
	- ...[install git](https://git-scm.com/downloads) on your laptop and check out [our repository](https://github.com/ShrimpingIt/cockle) if you are familiar with git and want to track future changes or contribute

* Download or unzip the repository contents to a location where you can find them. Launch a console and change to the directory containing the scripts. Now run...

	```python deployall.py```

* Unplug and replug your Cockle to restart it.

This should complete the process of downloading the Micropython image for your Cockle, uploading modules (libraries of code) to the Cockle, and optionally uploading a behaviour for the cockle to run on startup.

## Appendix B: Configuring Laptop for Serial Connection

If you are using a home machine, you will need to
* Ensure the [CP2102 USB to UART drivers](http://shrimping.it/drivers/cp2012) are installed
	* a restart of your machine is typically needed after this step
* Ensure [Python3](https://www.python.org/downloads/) is installed
	* Python version 3 is preferred, the same version as your badges will run, but Python 2 will do

After completing these steps you should be able to plug in your NodeMCU, (see under ```Powering Up```), then run a terminal or cmd.exe and enter the following...

    python -c "import serial.tools.list_ports;print serial.tools.list_ports.comports()"

If you have successfully completed configuring your laptop, the at least one serial port should be listed. If it reports ```[]``` (an empty list between square brackets), then the device or drivers have a problem.

on Linux it may report ```['ttyUSB0']``` or on Mac OS it may report ```['tty.SLAB_USBtoUART']```. On both Linux and Mac OS the full port name should be prefixed by ```/dev/``` making it ```/dev/ttyUSB0```.

On Windows it may report ```['COM4']```, meaning the Port Name is ```COM4```

If more than one port appears in the list, unplug and replug your NodeMCU, and identify which port  appears and disappears from the list.
