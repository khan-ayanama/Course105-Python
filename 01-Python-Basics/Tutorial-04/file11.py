numbers = [1, 2, 3, 4, 5]

# Using map() with a lambda function to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using filter() with a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
