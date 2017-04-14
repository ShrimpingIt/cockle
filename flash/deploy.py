import esptool
import config

flashLookupOverride = dict(
	baud=1500000
)

def flash_config():
	lookup = dict()
	lookup.update(config.hardware_config())
	lookup.update(config.filesystem_config())
	lookup.update(flashLookupOverride)
	return lookup

# do the erase
def erase():
	config.emulate_invocation("esptool.py --port ${port} erase_flash", flash_config())
	esptool.main()

# do the write
def flash():
	config.emulate_invocation("esptool.py --port ${port} --baud ${baud} write_flash --flash_mode dio --flash_size=4MB 0 ${local_image_path}", flash_config())
	esptool.main()
	
def run():	
	erase()
	flash()

if __name__ == "__main__":
	run()
