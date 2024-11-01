#Write a program to convert a string to uppercase.
def upper_case(string):
    """Convert a string to upper case and return the result."""
    return string.upper()

user_string = input("Enter any word/sentence: ")
upper_string = upper_case(user_string)
print(f"The converted word/sentence is {upper_string}")
