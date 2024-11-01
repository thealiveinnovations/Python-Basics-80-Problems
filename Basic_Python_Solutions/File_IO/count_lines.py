#Write a program to count the number of lines in a file.
from pathlib import Path

def count_lines(text_file):
    """Count lines of an existing file and return to the result."""
    path = Path (text_file)
    contents = path.read_text()
    line_count = len(contents.splitlines())
    return line_count

user_file = 'learning_python.txt'
len_user_file = count_lines(user_file)
print(f"\nThere is {len_user_file} lines in your file.")
