#Write a program to reverse a list.
def reverse_list(numbers):
    """Reverse the order of element of the list and return to the modified list."""
    numbers.reverse()
    return numbers

my_list = [5,10,14,7,2]
reverse_list_order = reverse_list(my_list)
print(reverse_list_order)
