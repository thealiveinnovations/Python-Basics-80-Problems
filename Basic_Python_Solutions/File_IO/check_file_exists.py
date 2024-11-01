#Write a program to check if a file exists.
from pathlib import Path

def check_file_exists(text_file):
    """Check a file exists or not and print the result."""
    path = Path(text_file)
    if path.exists() and path.is_file():
        print(f"\nThe file '{text_file}' exists.")
    else:
        print(f"\nThe file {text_file} doesn't exists.")

user_file = 'learning_python.txt'
check_user_file = check_file_exists(user_file)
