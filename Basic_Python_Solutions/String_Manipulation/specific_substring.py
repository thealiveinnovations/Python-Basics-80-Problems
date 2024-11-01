#Write a program to check if a string starts with a specific substring.
def check_starting_substring(string,substring):
    """Check if a string started with a specific substring or not."""
    return string.startswith(substring)

user_string = input("Enter a phrase/sentence: ")
user_substring = input("Enter the word you want to check: ")
check_substring = check_starting_substring(user_string,user_substring)
if check_starting_substring(user_string,user_substring):
    print(f"Your phrase/sentence starts with '{user_substring}' this word.")
else:
    print(f"Your phrase/sentence doesn't start with '{user_substring}' this word.")
    
