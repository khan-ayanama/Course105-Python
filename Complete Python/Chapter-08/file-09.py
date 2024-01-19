# Passing Lambda Function to another Function in Python 

# Function that takes a lambda function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

# Example lambda functions
add_lambda = lambda x, y: x + y
multiply_lambda = lambda x, y: x * y

# Using the function with lambda functions
result_addition = apply_operation(3, 4, add_lambda)
result_multiplication = apply_operation(3, 4, multiply_lambda)

print(result_addition)       # Output: 7
print(result_multiplication) # Output: 12
