#Write a program to check if a key exists in a dictionary.
my_dict = {'name':'john','city':'chicago','age':22}

def check_key(dictionary,key):
    """Check if the key exists in the dictionary."""
    if key in dictionary:
        return True
    else:
        return False
    
key_to_check = input("Enter the key to check: ")

if check_key(my_dict,key_to_check):
    print(f"\nThe key {key_to_check} exists in the dictionary.")
else:
    print(f"\nThe key {key_to_check} doesn't exists in the dictionary.")
    
