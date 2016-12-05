import os

image_name = "esp8266-20161110-v1.8.6.bin"

local_dir_path = os.path.dirname(os.path.realpath(__file__))
local_image_path = local_dir_path + "/firmwares/" + image_name

remote_dir_url = "http://micropython.org/resources/firmware/"
remote_image_url = remote_dir_url + image_name
