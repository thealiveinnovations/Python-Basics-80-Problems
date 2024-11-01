#Write a function to add two numbers and reeturn the result.
def sum_numbers(num_1,num_2):
    """Calculate sum of two numbers."""

    return num_1 + num_2

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

result = sum_numbers(num_1, num_2)

print(f"The sum of {num_1} and {num_2} is {result}")
