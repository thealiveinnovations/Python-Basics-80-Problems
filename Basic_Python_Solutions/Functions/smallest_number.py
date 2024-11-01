#Write a function that accepts a list of numbers and returns the smallest number.
def smallest_number(numbers):
    """Find the smallest number from the list and return the result."""
    min_num = float('inf')
    for number in numbers:
        if number < min_num:
            min_num = number
    return min_num

num_list = [5,8,7,3,4]
small_number = smallest_number(num_list)
print(f"The smallest number from the list is {small_number}")   
     
