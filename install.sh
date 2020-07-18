#!/usr/bin/env bash
rmdir lenv
python3 -m virtualenv lenv
source lenv/bin/activate
echo `which pip`
lenv/bin/python -m pip install --upgrade pip
lenv/bin/pip install -r requirements.txt

# Required for raspberry pi
sudo apt-get install libatlas-base-dev
