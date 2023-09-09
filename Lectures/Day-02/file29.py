# A lambda function in Python is a concise way to define small, anonymous functions. Lambda functions are also known as lambda expressions. These functions can take any number of arguments but can only have one expression. Lambda functions are useful when you need a simple function for a short period of time, and you don't want to define a full named function using the def keyword.

# lambda arguments: expression

# Lambda functions are typically used for simple operations, such as in functional programming constructs like map(), filter(), and sorted().

# Regular function
def add(x, y):
    return x + y

result1 = add(5, 10)
print(result1)  # Output: 15

# Equivalent lambda function
lambda_add = lambda x, y: x + y

result2 = lambda_add(5, 10)
print(result2)  # Output: 15

