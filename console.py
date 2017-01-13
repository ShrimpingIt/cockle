from serial.tools import miniterm
import sys
sys.argv = "miniterm.py --raw /dev/tty.SLAB_USBtoUART 115200".split()
miniterm.main()
