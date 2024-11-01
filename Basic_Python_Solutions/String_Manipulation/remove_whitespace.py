#Write a progarm to remove whitespace from the beginning and end of the string.
def remove_whitespace(string):
    """Remove any extra whitespace from the beginning and the end of the string."""
    return string.strip()

user_string = input("Enter any string with extra whitespace: ")
trimmed_string = remove_whitespace(user_string)
print(f"\nString after removing extra whitespace: {trimmed_string}")
