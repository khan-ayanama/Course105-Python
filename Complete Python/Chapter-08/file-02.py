# Nested Functions
def outer_function(x):
    # This is the outer function
    def inner_function(y):
        # This is the nested function
        return y * 2
    
    result = x + inner_function(x)
    return result

# Using the functions
output = outer_function(3)
print(output)  # Output: 9


# Passing function as parameter
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def process_numbers(numbers, operation):
    result = []
    for num in numbers:
        result.append(operation(num))
    return result

# Using the functions
numbers_list = [1, 2, 3, 4, 5]

# Pass the square function as a parameter
squared_numbers = process_numbers(numbers_list, square)
print("Squared Numbers:", squared_numbers)

# Pass the cube function as a parameter
cubed_numbers = process_numbers(numbers_list, cube)
print("Cubed Numbers:", cubed_numbers)
