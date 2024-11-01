#Write a program to check if a number is prime.
num = int(input("Enter any number: "))
not_prime_num = 0
prime_num = 0
is_prime = True
if num <= 1:
    print(f"The number {num} is not prime.")
else:
    end_num = int(num**0.5)
    for i in range(2,end_num+1):
        if num % i == 0:
            not_prime_num = int(num)
            print(f'\nThe number {not_prime_num} is not a prime number.')
            is_prime = False
            break
    if is_prime:
        prime_num = int(num)
        print(f'\nThe number {prime_num} is a prime number!')
