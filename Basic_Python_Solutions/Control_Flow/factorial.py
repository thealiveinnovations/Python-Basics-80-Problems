#Write a program to find the factorial of a number using a loop.
factorial = 1
num = int(input("Enter a number: "))

for n in range(1,num+1):
    factorial = factorial * n

print(f"\nThe factorial of the {num} is {factorial}")
