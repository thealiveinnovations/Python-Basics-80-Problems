#Write a program to find the union of two sets.
def union_sets(set_1,set_2):
    """Return the union of two sets."""
    return set_1.union(set_2)

my_set_1 = {1,2,3,4,5}
my_set_2 = {6,7,8,9,10}
union_myset = union_sets(my_set_1,my_set_2)
print(union_myset)
