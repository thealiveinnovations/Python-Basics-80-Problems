#Write a program to check if a string only contains numbers.
def string_num(string):
    """Check if a string contains only number and return the result."""
    nums = '0123456789'
    for char in string:
        if char in nums:
            return True
    return False

user_string = input("Enter anything: ")
check_string = string_num(user_string)
if check_string:
    print("\nYour string contains numbers!")
else:
    print("\nYour string doesn't contain any number.")
