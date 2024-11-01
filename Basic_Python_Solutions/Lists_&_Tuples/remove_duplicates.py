#Write a program to remove duplicates from a list.
def remove_duplicates(item_lists):
    """Remove the duplicate items from the list while preserving the order."""
    unique_list = []
    for item in item_lists:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

my_list = [1,3,7,1,2,3,1]
remove_dupe = remove_duplicates(my_list)
print(remove_dupe)  
