#Write a program to find the largest number in a list.
def largest_num(nums):
    """Find the largest number from the list and return the result."""
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

user_list = [5,7,8,10,14,3,2]
large_num = largest_num(user_list)
print(f"\nThe largest number from the list is {large_num}")        
