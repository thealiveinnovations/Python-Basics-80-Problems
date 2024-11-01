#Write a program to find the maximum of three numbers.
def maximum_num(num_1,num_2,num_3):
    """Calculate the maximum between three numbers."""
   
    if num_1 >= num_2 and num_1 >= num_3:
        return num_1
    elif num_2 >= num_1 and num_2 >= num_3:
        return num_2
    else:
        return num_3

num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

max_num = maximum_num(num_1,num_2,num_3)
    
print(f"\n{max_num} is the maximum between {num_1},{num_2} and {num_3}")
