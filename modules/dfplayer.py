from machine import UART
from time import sleep

uart = UART(1, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

def split(num):
    return num >> 8, num & 0xFF

def execute(CMD, Par1, Par2):
    Start_Byte=0x7E
    Version_Byte=0xFF
    Command_Length=0x06
    Acknowledge=0x00
    End_Byte=0xEF
    Checksum = -(Version_Byte + Command_Length + CMD + Acknowledge + Par1 + Par2)
    HighByte, LowByte = split(Checksum)
    CommandLine = bytes([b & 0xFF for b in [Start_Byte, Version_Byte, Command_Length, CMD, Acknowledge,
        Par1, Par2, HighByte, LowByte, End_Byte
    ]])
    uart.write(CommandLine)

def init():
      execute(0x3F, 0x00, 0x00)

def play(dirNum, fileNum):
    execute(0x0F,dirNum,fileNum)

def volume(val=0x30):
    execute(0x06,0x00,val)  

init()
sleep(5)
volume(0x30)
folder = 1
while True:
    for track in range(1, 7):
        play(folder,track)
        sleep(10)
