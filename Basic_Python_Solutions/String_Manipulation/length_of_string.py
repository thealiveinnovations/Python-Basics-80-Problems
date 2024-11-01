#Write a program to find the length of a string without using len().
def length_string(string):
    """Count the length of a string and return the result."""
    count = 0
    for char in string:
        count += 1
    return count

user_string = input("Enter a word/phrase: ")
user_string_length = length_string(user_string)
print(f"The length of your word/phrase is {user_string_length}") 
