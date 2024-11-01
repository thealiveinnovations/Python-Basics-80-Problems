#Write a class with a method that calculates the area of a rectangle.
class Area:
    """A simple attempt to calculate area."""

    def __init__(self,length,width) -> None:
        """Initialize the attributes of class area."""
        self.length = length
        self.width = width

    def calculate_area(self):
        """Calculate the area of a rectangle and return to the result."""
        rectangle_area = self.length * self.width
        return rectangle_area
    
rectangle = Area(14,7)
print(rectangle.calculate_area())
