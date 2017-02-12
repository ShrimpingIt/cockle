#!/bin/bash
cd micropython
#python retrieve.py
#python deploy.py
ampy --port /dev/ttyUSB0 reset
cd ../
cd modules
python deploy.py
cd ../
cd replserver
python deploy.py
cd ../
echo "Uploading 'main.py' file"
ampy --port /dev/ttyUSB0 put regimes/01_shiftregister/main.py
