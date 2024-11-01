#Write a program to merge two lists into one.
def merge_list(list_1,list_2):
    """Merge two lists using + opertor."""
    return list_1 + list_2

my_list1 = [1,2,3]
my_list2 =[4,5,6]
merge_mylist = merge_list(my_list1,my_list2)
print(f"Merged list: {merge_mylist}")
