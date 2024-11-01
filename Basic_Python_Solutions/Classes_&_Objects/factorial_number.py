#Write a class with a method that returns the factorial of a number.
class MathematicalOperations:
    """A simple class to prform mathematical operations."""

    def __init__(self):
        """Initialize the class."""
        pass

    def calculate_factorial(self,num):
        """Calculate the factorial of a specific number and return to the result."""
        if num == 0 or num == 1:
            return 1
        else:
            result = 1
            for i in range(2,num+1):
                result *= i
        return result
    
math_factorial = MathematicalOperations()
number = 5
print(f"\nThe factorial of {number} is {math_factorial.calculate_factorial(number)}")
