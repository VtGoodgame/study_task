#!/bin/bash

if python --version | grep -q "Python 3"; then
    echo "Python 3 is installed."
else
    echo "Python 3 is not installed. Please install Python 3 to run this script."
    exit 1
fi

python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python main.py 