#Write a program to delete a file.
import os

def delete_file(text_file):
    """Delete an existing file."""
    try:
        os.remove(text_file)
        print(f"\nThe file {text_file} has been removed.")
    except FileNotFoundError:
        print(f"\nThe file {text_file} doesn't exists.")
    except PermissionError:
        print(f"\nPermission denied: Can't delete {text_file}")

user_file = 'moby_dick.txt'
delete_file(user_file)
