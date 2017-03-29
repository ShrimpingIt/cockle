import sys
from serial.tools import miniterm
import config

minicomCommand = "serial.tools.miniterm --raw --encoding ascii ${port} ${baud}"
minicomLookup = config.hardware_config()
config.emulate_invocation(minicomCommand, minicomLookup)
miniterm.main()

