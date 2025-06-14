# Password Pwned Checker

Check if your passwords have been compromised without revealing them, using HIBP’s secure API via a simple CLI tool.

## Features

- Uses the k-Anonymity model: only sends the first 5 characters of your password's SHA-1 hash, keeping your full password private.
- Checks if a password has appeared in known data breaches.
- Lightweight and easy to use CLI interface.
- No external database required, all queries are done live.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-pwned-checker.git
   cd password-pwned-checker
   ```
