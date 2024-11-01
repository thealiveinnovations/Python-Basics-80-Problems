# Write a function that converts a given temperature from Fahrenheit to Celsius. 
def celcius(fahrenheit):
    """Calculate the fahrenheit value to celcius and return the result."""
    celcius = (fahrenheit - 32) * (5/9)
    rounded_celcius = round(celcius,2)
    return rounded_celcius

fah_temp = int(input("Enter temparature in fahrenheit: "))
result = celcius(fah_temp)
print(f"\nThe temparature in celcius is {result}")
