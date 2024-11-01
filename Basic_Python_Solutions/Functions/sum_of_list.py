#Write a function to find the sum of a list of numbers.
def sum_numbers(numbers):
    """Calculate the sum of a list of numbers."""
    total = 0
    for number in numbers:
        total += number
    return total
    
my_list = [23,45,67,32,65,78,23,78]
sum = sum_numbers(my_list)
print(f"\nThe sum of numbers {sum}")
    
