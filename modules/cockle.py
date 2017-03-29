from machine import Pin
from os import urandom
from math import floor
from time import sleep_ms

pins = [
    Pin(16),
    Pin(5),
    Pin(4),
    Pin(0),
    Pin(2),
    Pin(14),
    Pin(12),
    Pin(13),
    Pin(15),
    Pin(3),
    Pin(1),
]

'''
Efficient calculation for the logarithm (to the base 2) of val, rounded 
up to the next whole number. It rounds down val, then unsets individual bits
until val is 0. The final bit unset is the largest power of 2 in val, 
allowing us to calculate an upper bound on the logarithm. [Cefn Hoile]
'''			
def log2approx(val):
	val = floor(val)
	approx = 0
	while val != 0:
		val &= ~ (1<<approx)
		approx = approx + 1
	return approx
		
'''
Calculates a 'uniformly' distributed random integer up to and excluding bound. 
Draws enough bytes from the random number generator for every possible bit up 
to the bound to be populated, plus an extra byte. Sequencing these bytes creates 
a number at least 256 times larger than the target bound. It then calculates the 
modulus of this number to produce an integer result within bounds. [Cefn Hoile]
'''
def randint(minVal, maxVal=None):
	if(maxVal!=None):
		return minVal + randint(maxVal-minVal)
	else:
		maxVal=minVal		
	byteCount = (log2approx(maxVal) // 8) + 1 # each byte is 8 powers of two
	val = 0
	for idx, entry in enumerate(bytearray(urandom(byteCount))):
		val |= entry << (idx * 8)
	return val % maxVal

def sleep(ms):
	return sleep_ms(ms)