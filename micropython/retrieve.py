import os
import requests
from config import remote_image_url, local_image_path

def get_firmware():
	# retrieve from url, write to local path
	r = requests.get(remote_image_url, stream=True)
	with open(local_image_path, 'wb') as f:
		for chunk in r.iter_content(chunk_size=1024): 
			if chunk:
				f.write(chunk)

get_firmware()
