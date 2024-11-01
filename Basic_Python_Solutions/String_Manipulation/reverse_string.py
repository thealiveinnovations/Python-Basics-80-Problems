#Write a program to reverse a string.
def reverse_string(word):
    """Reverse a string and return to the converted string."""
    reversed_word = word[::-1]
    return reversed_word

user_word = input("Enter any number/phrase: ")
converted_word = reverse_string(user_word)
print(f"Here is your reversed word/phrase '{converted_word}' ")
