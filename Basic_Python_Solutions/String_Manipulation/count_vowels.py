#Write a program to count the number of vowels in a string.
def count_vowels(string):
    """Count the number of the vowels from the string and return the result."""
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

user_string = input("Enter a word/phrase: ")
user_string_vowel = count_vowels(user_string)
print(f"\nThere is {user_string_vowel} vowels in your word/phrase.")
