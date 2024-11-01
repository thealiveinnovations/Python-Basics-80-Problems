#Create a dog class with attributes like name and breed.Add a method to make the dog bark.
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self,name,breed):
        """Initialize the attributes of class dog."""
        self.name = name
        self.breed = breed

    def bark(self):
        """Simulate a dog barking."""
        print(f"{self.name} is barking.")

my_dog = Dog('Bob','GSD')
my_dog.bark()
