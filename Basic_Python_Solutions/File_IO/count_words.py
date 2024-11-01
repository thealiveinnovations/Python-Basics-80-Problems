#Write a program to count the number of words in a file.
from pathlib import Path

def count_words(text_file):
    """Count words from an existing file."""
    try:
        path = Path(text_file)
        contents = path. read_text(encoding='utf-8')
    except FileNotFoundError:
        print("\nSorry! The file doesn't exist.")
        return 0
    except UnicodeDecodeError:
        print("\nError decoding this file! Please check the file encoding.")
        return 0
    else:
        words = contents.split()
        num_words = len(words)
        return num_words
    
user_file = 'alice.txt'
words_uesr_file = count_words(user_file)
print(f"\nYour file has {words_uesr_file} words!")
    
