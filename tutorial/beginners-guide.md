# Beginners Guide

A quick write up to get you started.

## Conneting up

Attach your 8 LED strip so that...

* GND connects to G on the cockle
* DIN connection to pin 2 on the cockle
* 5v connects to 3V on the cockle


## Powering up connecting and lighting your first LED

* Connect your cockle by USB to your computer
* Look in your list of WiFi connections for one listed as MicroPython-xxxx (where xxxx is a number)
* Connect to this WiFi network (the password will be "micropythoN" without the speech marks)
* Open a web browser
* Navigate to http://192.168.4.1
* If this doesn't connect wait a few moments and try again, the Cockle takes a few minutes to come up
* Once the page loads click "Connect" at the top left
* Enter the password "shrimping"
* Enter ```setPixel(1, red)``` and you should see the first pixel on your strip light up red
* Enter ```setPixel(7, yellow)``` and the last pixel should light up yellow
* Enter ```clearPixels()``` and the all the LEDs should go off


## Firing up a function
* Enter ```rainbow()``` and your LED strip should light up like a rainbow!
* Enter ```def hue_to_rgb(h):```
* Enter ```return hsb_to_rgb(h, 0.5, 0.5)```
* Press return three or four times until you get back to the >>> prompt
* Enter ```rainbow()``` again.  You've overwritten the hue_to_rgb function and now you have a pastel rainbow
 
