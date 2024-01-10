# Function returning another function
def outer_function(power):
    # This is the outer function
    def inner_function(x):
        # This is the inner function
        return x ** power
    
    return inner_function

# Using the functions
square_function = outer_function(2)
cube_function = outer_function(3)

# Applying the returned functions
result_square = square_function(4)  # 4^2 = 16
result_cube = cube_function(3)     # 3^3 = 27

print("Square:", result_square)
print("Cube:", result_cube)


# Formal Argument:
# Function defination parameters are called formal arguments

# Actual Argument:
# Function call arguments are actual arguments