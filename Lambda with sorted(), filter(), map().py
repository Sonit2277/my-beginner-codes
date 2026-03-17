numbers = [5, 2, 8, 1, 9, 3]

# Sort by remainder when divided by 3
sorted_numbers = sorted(numbers, key=lambda x: x % 3)
print("Sorted by remainder when divided by 3:", sorted_numbers)

# Filter only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))  

# Map: square every number
squared_numbers = map(lambda x: x ** 2, numbers)
print("Squared numbers:", list(squared_numbers))