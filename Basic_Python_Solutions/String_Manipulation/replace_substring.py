#Write a program to replace all occurrencs of a substring in a string.
def replace_substring(original_string, old_substring, new_substring):
    """Replace all the occurrences of old substring with new one and return the converted original string."""
    return original_string.replace(old_substring,new_substring)

user_string = input("Enter any phrase/sentence: ")
old_user_string = input("Enter the word you want to replace: ")
new_user_string = input("Enter the new word: ")
replaced_string = replace_substring(user_string,old_user_string,new_user_string)
print(f"Here is your converted phrase/sentence '{replaced_string}'")
