#Write a program to find the size of a file.
import os

def file_size(text_file):
    """Return the size of a file in bytes."""
    try:
        size = os.path.getsize(text_file)
        print(f"\nThe size of the file '{text_file}' is {size} bytes.")
        return size
    except FileNotFoundError:
        print(f"\nThe file '{file_size}' no found.")
    except Exception as e:
        print(f"\nError: {e}")

my_file = 'alice.txt'
my_file_size = file_size(my_file)
