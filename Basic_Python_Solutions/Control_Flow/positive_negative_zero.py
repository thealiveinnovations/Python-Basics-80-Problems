#Write a program to check if a number is positive,negative or zero.
num = int(input("Enter a number: "))

if num == 0:
    print("\nThe number is zero!")
elif num > 0:
    print("\nThis is a positive number.")
elif num < 0:
    print("\nThis is a negative number.")
