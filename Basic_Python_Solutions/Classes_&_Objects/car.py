#Create a car class with attributes like make,model and year. Create an object of this class. 
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
    
my_car = Car('tesla','model s','2022')
print(my_car.descriptive_name())
