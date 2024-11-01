#Write a program to find the smallest number in a list.
def smallest_num(nums):
    """"Find the smallest number from a list and return the result."""
    min_num = float('inf')
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

user_list = [5,7,8,10,14,2,3]
small_num = smallest_num(user_list)
print(f"\nThe smallest number from the list is {small_num}")        
