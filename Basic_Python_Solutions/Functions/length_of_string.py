#Write a function to return the length of the string.
def string_length(string):
    """Calculate the length of the string and return the result."""
    len_string = len(string)
    return len_string

user_string = input("Enter a word/sentence: ")
length = string_length(user_string)
print(f"The length of your word is {length}") 
