import config
import esptool

# do the erase
config.emulateInvocation("esptool.py --port ${port} erase_flash")
esptool.main()

# do the write
config.emulateInvocation("esptool.py --port ${port} --baud ${baud} write_flash --flash_mode dio --flash_size=32m 0 ${local_image_path}")
esptool.main()
