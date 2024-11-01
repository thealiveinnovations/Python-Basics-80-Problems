#Write a function that returns the nth fibonacci number.
def fibonacci(num):
    """Return the nth fibonacci number."""
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
user_num = int(input("Enter the value of n: "))
fib_num =fibonacci(user_num)
print(f"\n{fib_num}")
