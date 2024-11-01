#Write a program to convert Celcius to Fahrenheit.
celcius = float(input("Enter the temparature in Celcius: "))
divide_value = 9/5
fahrenheit = (divide_value * celcius) + 32
rounded_fahrenheit = round(fahrenheit,2)

print(f"The temparature in Fahrenheit is {rounded_fahrenheit}")
