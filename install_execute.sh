#!/usr/bin/env bash

python3 -m venv venv
. venv-datapred/bin/activate
pip install -r requirements.txt
ipython kernel install --user --name=venv
jupyter notebook
