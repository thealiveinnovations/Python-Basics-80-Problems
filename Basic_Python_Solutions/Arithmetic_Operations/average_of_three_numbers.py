#Write a program to calculate the avarage of three numbers.
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))
num_3 = float(input("Enter the third number: "))

sum_nums = num_1 + num_2 + num_3
average = sum_nums / 3
rounded_average = round(average,2)

print(f"\nThe average of three number is {rounded_average}")
