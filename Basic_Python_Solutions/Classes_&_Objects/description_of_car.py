#Write a class method to print out description of the car.
class Car:
    """A simple attempt to model a car."""

    def __init__(self,make,model,year) -> None:
        """Initialize the attributes of car."""
        self.make = make
        self.model = model
        self.year = year

    def descriptive_name(self):
        """Return a neatly formatted description of the car."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def description(self):
        """Return a description for the specific car."""
        get_description = f"The {self.year} {self.make} {self.model} is a remarkable vehicle with advanced features."
        return get_description
    
my_car = Car('tesla','model s','2022')
print(my_car.descriptive_name())
print(my_car.description())
