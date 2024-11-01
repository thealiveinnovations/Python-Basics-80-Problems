#Write a program to print the multiplication table of a number
multiplication = 0

num = int(input("Which number's multiplication table you want? "))
end = int(input("How many multiplication you want? "))

for n in range(0,end+1):
    multiplication = num * n
    print(f"{num} X {n} = {multiplication}")
