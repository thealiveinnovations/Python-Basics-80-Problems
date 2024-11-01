#Write a function to count the number of vowels in a string.
def vowel_str(string):
    """Count the vowels of a string and return the result."""
    vowels = 'aeiouAEIOU'
    count = 0

    for vowel in vowels:
        if vowel in string:
            count += 1
    return count

user_string = input("Enter a word/sentence: ")
result = vowel_str(user_string)
print(f"\nThe number of vowels in your word is {result}")       
