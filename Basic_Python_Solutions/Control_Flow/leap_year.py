#Write a program to check if a given year is leap year.
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"\nThe year {year} is a leap year!")
        else:
            print(f"\nThe year {year} is not a leap year.")
    else:
        print(f"\nThe year {year} is a leap year!")
else:
    print(f"\nThe year {year} is not a leap year.")
