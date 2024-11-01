#Write a class with a method that returns the square of number.
class SimpleMath:
    """A simple attempt to solve mathematical problems."""

    def __init__(self,num,power) -> None:
        """Initialize the attributes of simplemath."""
        self.num = num
        self.power = power

    def calculate_power(self):
        """Return the result of the square of a number."""
        result = self.num ** self.power
        return result
    
math_operation = SimpleMath(5,2)
print(math_operation.calculate_power())
