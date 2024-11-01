#Write a program to find the square root of a number.
import math

num = float(input("Enter a number: "))
square_root_num = math.sqrt(num)

# square_root_num = num ** 0.5
rounded_square_root_num = round(square_root_num,2)

print(f"Both positive and negetive value of {rounded_square_root_num} is square root of {num}")
