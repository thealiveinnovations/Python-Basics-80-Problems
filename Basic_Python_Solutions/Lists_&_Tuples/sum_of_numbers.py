#Write a program to calculate the sum of all numbers in a list.
def sum_nums(nums):
    """Calculate the sum of all numbers in the list and return the result."""
    sum = 0
    for num in nums:
        sum += num
    return sum

user_list = [5,7,8,10,14,3,2]
sum = sum_nums(user_list)
print(f"The sum of the numbers in the list is {sum}")
