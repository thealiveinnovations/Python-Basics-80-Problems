#Write a program to remove duplicates from a list using a set.
def remove_duplicates(input_list):
    """Remove duplicates from the list and return the unique list."""
    unique_items = set(input_list)
    return list(unique_items)

my_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
unique_list = remove_duplicates(my_list)
print(unique_list)
