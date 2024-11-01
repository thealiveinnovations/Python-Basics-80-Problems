#Write a program to append text to an existing file.
from pathlib import Path

def append_text(text_file,text):
    """Append a new text into a existing file."""
    path = Path(text_file)
    content = path.write_text(text)
    return content

user_text = 'One day I will bring revolutions in AI!'
user_text += '\nI am working so hard everyday to bring that day sooner!'
user_text += '\nI am building the foundation of my dream day by day.'
append_text('writing.txt',user_text)
