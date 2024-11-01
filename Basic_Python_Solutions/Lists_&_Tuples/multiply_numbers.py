#Write a program to multiply all numbers in a list.
def multiply_nums(nums):
    """Mutiply the numbers from the list and return the result."""
    multiply = 1
    for num in nums:
        multiply = multiply * num
    return multiply

user_list = [5,7,8,10,14,3,2]
result = multiply_nums(user_list)
print(f"The multiplication of the numbers is {result}")    
