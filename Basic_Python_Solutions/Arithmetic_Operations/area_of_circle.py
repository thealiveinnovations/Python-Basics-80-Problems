#Write a program to find the area of a circle given it's radius.
pi_value = 3.1416
radius = float(input("Enter the radius of the circle: "))

square_radius = radius**2
circle_area = pi_value * square_radius

print(f"\nThe area of the circle is {circle_area}.")
