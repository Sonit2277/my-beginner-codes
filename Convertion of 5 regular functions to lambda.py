square= lambda x: x**2
#use the lambda function to calculate the square of a number

#example usage
print(square(5))

is_even = lambda x: x % 2 == 0
#use the lambda function to check if a number is even   

#example usage
print(is_even(4))
print(is_even(5))

add = lambda x, y: x + y
#use the lambda function to add two numbers

#example usage
print(add(3, 4))
print(add(10, 20))

celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
#use the lambda function to convert Celsius to Fahrenheit

#example usage
print(celsius_to_fahrenheit(0))  # Freezing point of water
print(celsius_to_fahrenheit(100))  # Boiling point of water

reverse_string = lambda s: s[::-1]
#use the lambda function to reverse a string

#example usage
print(reverse_string("Hello, World!"))
print(reverse_string("Python"))
