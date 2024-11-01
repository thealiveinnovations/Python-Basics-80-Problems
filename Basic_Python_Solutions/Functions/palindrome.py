#Write a function to check if a string is a palindrome.
def check_palindrome(s):
    """Check if a string is a palindrome or not."""
    
    normalized_string = s.replace(" ","").lower()
    reversed_string = normalized_string[::-1]
    return reversed_string

get_s = input('Enter any word: ')
reverse_s = check_palindrome(get_s)
print(f"The palindrome of the word is {reverse_s}")
