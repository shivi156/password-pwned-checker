#!/bin/bash

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate the virtual environment
source venv/bin/activate

# Just install requirements, no pip upgrade
pip install -r requirements.txt

# Run the password checker
python password_pwned_checker.py
