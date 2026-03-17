numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares of all numbers
sqrt = [x**2 for x in numbers]
print("Squares of all numbers:", sqrt)

# only even numbers
even_sqrt = [x**2 for x in numbers if x % 2 == 0]
print("Squares of even numbers:", even_sqrt)

# only numbers divisible by 3
divisible_by_3_sqrt = [x**2 for x in numbers if x % 3 == 0]
print("Squares of numbers divisible by 3:", divisible_by_3_sqrt)

# squares of even numbers only
even_only_sqrt = [x**2 for x in numbers if x % 2 == 0]
print("Squares of even numbers only:", even_only_sqrt)

# squares of odd numbers only
odd_only_sqrt = [x**2 for x in numbers if x % 2 != 0]
print("Squares of odd numbers only:", odd_only_sqrt)