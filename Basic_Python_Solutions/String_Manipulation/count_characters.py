#Write a program to count the number of characters in a string.
def count_char(string):
    """Count the character of the given string and return to the count."""
    string_without_space = string.replace(" ","")
    return len(string_without_space)

user_string = input("Enter any word/sentence: ")
char_no = count_char(user_string)
print(f"The word/sentence has {char_no} characters.")
