# Returning Lambda Function from a Function in Python 

# Function that returns a lambda function
def create_multiplier(factor):
    return lambda x: x * factor

# Example usage
double = create_multiplier(2)
triple = create_multiplier(3)

result_double = double(5)
result_triple = triple(5)

print(result_double)  # Output: 10
print(result_triple)  # Output: 15
