@echo off

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Run the password checker
python password_pwned_checker.py

pause
