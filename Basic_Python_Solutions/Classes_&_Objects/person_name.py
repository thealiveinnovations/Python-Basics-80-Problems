#Create a person class with first_name and last_name attributes. Create an object and print the person's full name.
class PersonInfo:
    """A simple attempt torepresent a person."""
    
    def __init__(self,first_name,last_name) -> None:
        """Initialize the attributes of personinfo class."""
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Return a neatly formatted full name."""
        long_name = f"{self.first_name} {self.last_name}"
        return long_name.title()
    
my_info = PersonInfo('emma','watson')
print(my_info.full_name())
