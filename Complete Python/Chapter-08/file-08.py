# Nested Lambda functions

# Nested lambda functions
outer_lambda = lambda x: (lambda y: x + y)

# Usage
add_five = outer_lambda(5)
result = add_five(3)
print(result)  # Output: 8
