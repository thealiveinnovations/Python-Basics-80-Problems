#Write a program to create a new file and write some text to it.
from pathlib import Path

def write_file(txt_file,text):
    """Create a new file and write some content into it."""
    path = Path(txt_file)
    content = path.write_text(text)
    return content

user_text = 'I will achieve my dreams one day!'
write_file('writing.txt',user_text)
