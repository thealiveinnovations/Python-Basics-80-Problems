#Write a program to read a file and print it's content.
from pathlib import Path

def read_file(txt_file):
    """Read a file and print it's content."""
    path = Path(txt_file)
    content = path.read_text()
    print(content)
    
read_file('learning_python.txt')
