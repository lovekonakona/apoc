#!/bin/sh

export PYTHONPATH=$PYTHONPATH:./src

. venv/bin/activate 

export MOUSE_RUNTIME=production

HOME=`pwd`
cd src
python apoc/web/main.py --running_dir=$HOME --port=8888
