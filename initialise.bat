@echo off

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip and install requirements
pip install -r requirements.txt > /dev/null 2>&1

REM Run the password checker
python password_pwned_checker.py

pause
