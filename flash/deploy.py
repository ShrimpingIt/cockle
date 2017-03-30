import esptool
import config

def flash_config():
	lookup = dict()
	lookup.update(config.hardware_config())
	lookup.update(config.filesystem_config())
	return lookup

# do the erase
def erase():
	config.emulate_invocation("esptool.py --port ${port} erase_flash", flash_config())
	esptool.main()

# do the write
def flash():
	config.emulate_invocation("esptool.py --port ${port} --baud ${baud} write_flash --flash_mode dio --flash_size=32m 0 ${local_image_path}", flash_config())
	esptool.main()
	
def run():	
	erase()
	flash()

if __name__ == "__main__":
	run()
