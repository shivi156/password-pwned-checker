import hashlib
import requests
import getpass

HIBP_API_PREFIX = "https://api.pwnedpasswords.com/range/"

def get_password_hash(password: str) -> str:
    """Return the SHA-1 hash of the password in uppercase."""
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1

def query_api(prefix: str) -> str:
    """Query the HIBP API with the first 5 chars of the SHA-1 hash."""
    url = HIBP_API_PREFIX + prefix
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f"Error fetching data from API: {response.status_code}")
    return response.text

def check_password_pwned(password: str) -> int:
    """
    Check how many times the password has appeared in breaches.
    Returns the count or 0 if not found.
    """
    sha1_hash = get_password_hash(password)
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    response = query_api(prefix)

    hashes = (line.split(':') for line in response.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            return int(count)
    return 0

def main():
    print("Password Pwned Checker — check if your password has been exposed.")
    password = getpass.getpass("Enter the password to check: ")
    count = check_password_pwned(password)

    if count:
        print(f"⚠️  Oh no — this password has been seen {count} times before!")
    else:
        print("✅ Good news — this password was NOT found in the database.")

if __name__ == "__main__":
    main()
