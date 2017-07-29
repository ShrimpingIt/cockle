from machine import Pin
from os import urandom
from math import floor
from utime import sleep_ms, ticks_ms, ticks_diff

uplink = None


pins = [
    Pin(16), #D0
    Pin(5),  #D1 PWM
    Pin(4),  #D2
    Pin(0),  #D3 PWM
    Pin(2),  #D4 PWM
    Pin(14), #D5 PWM
    Pin(12), #D6 PWM
    Pin(13), #D7 PWM
    Pin(15), #D8 PWM
    Pin(3),  #D9
    Pin(1),  #D10
]

def connect(ssid,auth,timeout=16000):
    from network import WLAN, STA_IF, AP_IF
    global uplink
    uplink = WLAN(STA_IF)
    uplink.active(True)
    uplink.connect(ssid, auth)
    started= ticks_ms()
    while True:
        if uplink.isconnected():
            return True
        else:
            if ticks_diff(ticks_ms(), started) < timeout:
                sleep_ms(100)
                continue
            else:
                return False

def https_get(url, headers=None):
    _, _, host, path = url.split('/', 3)
    import usocket
    import ussl
    addr = usocket.getaddrinfo(host, 443)[0][-1]
    s=usocket.socket()
    s.connect(addr)
    s.settimeout(1.0)
    try:
        s=ussl.wrap_socket(s)
        s.write(b'GET /{} HTTP/1.1\r\nHost: {}\r\nUser-Agent: Cockle\r\n'.format(path, host))
        if headers is not None:
            s.write(headers)
        s.write(b'\r\n')
        buf = bytearray(128)
        while True:
            gc.collect()
            try:
                count = s.readinto(buf) # TODO use readline for headers including e.g. 'content-length: 2358' then after blank line, count bytes before close
                if count > 0:
                    if count < len(buf):
                        sys.stdout.write(buf[:count])
                    else:
                        sys.stdout.write(buf)
                    continue
                else:
                    print("Count not greater than 0")
            except OSError as ose:
                print(ose)
            break
    finally:
        s.close()

def mac():      
    from network import WLAN
    nw = WLAN()
    return nw.config('mac') # 5 bytes

def showhex(bytearr):
    return "".join(['%.2x' % b for b in bytearr])

def identify(numBytes = None):
    add = mac()
    if numBytes == None:
        numBytes = len(add)
    return showhex(add[-numBytes:])
        
def suffix():
    return identify(3)

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
