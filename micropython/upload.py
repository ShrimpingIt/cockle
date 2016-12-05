import sys
import esptool
import config
from string import Template

port = "/dev/ttyUSB0"
baud = 115200

# do the erase
eraseTemplate = Template("esptool.py --port ${port} erase_flash")
eraseCommand = eraseTemplate.substitute(
	port=port
)
sys.argv = eraseCommand.split()
esptool.main()


# do the write
writeTemplate = Template("esptool.py --port ${port} --baud ${baud} write_flash --flash_mode dio --flash_size=32m 0 ${firmware}")
writeCommand = writeTemplate.substitute(
	firmware=config.local_image_path,
	port=port,
	baud=baud,
)
sys.argv = writeCommand.split()
esptool.main()

