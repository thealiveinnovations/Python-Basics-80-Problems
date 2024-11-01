#Write a function that calculates the factorial of a number using recursion.
def factorial(n):
    """Calculate factorials of a specific number and return the result."""
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
result = factorial(5)
print(f"The factorial of 5 is {result}")
