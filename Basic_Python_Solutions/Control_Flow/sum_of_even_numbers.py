#Write a program to find sum of all even numbers from 1 to 100.
sum = 0

for num in range (1,101):
    if num % 2 == 0:
        sum = sum + num
print(f"\nThe sum of even numbers from 1 to 100 is {sum}")
