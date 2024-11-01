#Write a program to find the index of the first occurrence of a substring.
def find_substring_index(original_string,substring):
    """Find the index of first occurrence of the substring and return to the result."""
    return original_string.find(substring)

user_string = input("Enter a phrase/sentence: ")
user_substring = input("Enter the word you want to find: ")
substring_index = find_substring_index(user_string,user_substring)
if substring_index != -1:
    print(f"Your word is found at the index of {substring_index}")
else:
    print(f"Your word is not found in the phrase/sentence.")
    
