#Write a program to find the perimeter of a rectangle given it's length and width.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

sum_values = length + width
perimeter = sum_values * 2
rounded_perimeter = round(perimeter,2)

print(f"The perimeter of the rectangle is {rounded_perimeter}")
