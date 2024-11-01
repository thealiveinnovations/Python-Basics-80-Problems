#Write a class with a static method to check if a number is even or odd.
class MathOperations:
    """A simple class to perform math operations."""
    
    @staticmethod
    def check_even_odd(num):
        """Check a specific number is even or odd."""
        if num % 2 == 0:
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")

MathOperations.check_even_odd(13)
