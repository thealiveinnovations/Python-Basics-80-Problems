#Write a program to read a file line by line and print each line.
from pathlib import Path

def read_each_line(text_file):
    """Read an existing file line by line and print each line."""
    try:
        path = Path(text_file)
        contents = path.read_text()
        lines = contents.splitlines()

        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"\nThe file {text_file} doesn't exists.")
    except IOError as e:
        print(f"\nError: {e}")

my_file = 'learning_python.txt'
every_line = read_each_line(my_file)
