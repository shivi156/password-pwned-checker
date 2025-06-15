# Password Pwned Checker

Python CLI tool to check if your passwords have been compromised.

## ✨ Features

- ✅ Check if a password has appeared in data breaches
- 🔒 Never sends your full password — only the first 5 chars of its SHA-1 hash
- 📦 Simple CLI tool, no account or API key needed
- 🛡️ Built with Python using HIBP’s public and secure API

## Demo

$ bash initialise.sh
Password Pwned Checker — check if your password has been exposed.
Enter the password to check:
⚠️ Oh no — this password has been seen 47897 times before!

## Project Structure

password-pwned-checker/
├── initialise.sh # Setup script (Linux/MacOS)
├── initialise.bat # Setup script (Windows)
├── password_pwned_checker.py # Main Python script
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Installation

git clone https://github.com/yourusername/password-pwned-checker.git
cd password-pwned-checker

Run the script to set up and launch:
For Linux/MaxOS:
bash initialise.sh
