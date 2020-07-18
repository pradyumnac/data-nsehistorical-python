#!/usr/bin/env bash
rmdir lenv
python3 -m virtualenv lenv
source lenv/bin/activate
echo `which pip`
wenv\bin\python -m pip install --upgrade pip
wenv\bin\pip install -r requirements.txt
