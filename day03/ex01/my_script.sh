#!/bin/sh

virtualenv local_lib --python=python3.9 ; source local_lib/bin/activate
pip3 --version
pip3 install git+https://github.com/jaraco/path.py.git -I --log install.log
python3 my_program.py