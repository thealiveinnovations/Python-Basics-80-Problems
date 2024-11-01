#Write a program to copy the contents of one file to another file.
from pathlib import Path

def copy_contents(source_file,destination_file):
    """Copy contents from one file to another file."""
    try:
        source_path = Path(source_file)
        destination_path = Path(destination_file)

        contents = source_path.read_text()
        destination_path.write_text(contents)

        print(f"Contents copied from {source_file} to {destination_file}")
    except FileNotFoundError:
        print(f"\nError: The file '{source_file}' doesn't exists.")
    except IOError as e:
        print(f"\nError: {e}")


my_source_file = 'learning_python.txt'
my_destination_file = 'copy_learning_python.txt'
copy_contents(my_source_file,my_destination_file)
