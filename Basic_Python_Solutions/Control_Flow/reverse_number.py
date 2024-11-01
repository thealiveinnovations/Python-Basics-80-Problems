#Write a program to reverse a number.
reversed_number = 0
num = int(input("Enter a number: "))

while num != 0:
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num //= 10

print(f"The reversed number is: ")
print(reversed_number,end='')
