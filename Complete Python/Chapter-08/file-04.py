# Actual Arguments:
# 1. Positional Argument
# 2. Keyword Arguments
# 3. Default Arguments
# 4. Variable Length Arguments
# 5. Keyword Variable Length Arguments


# Positional Arguments
def greet(name, greeting):
    return f"{greeting}, {name}!"

# Calling the function with positional arguments
result = greet("Boss", "Hello")
print(result)


# Keyword Arguments
# Keyword's arguments name and formal argument's name must match
# Number of arguments must be equal in formal and actual
def greet(name, greeting):
    return f"{greeting}, {name}!"

# Calling the function with keyword arguments
result = greet(name="Boss", greeting="Hello")
print(result)


# Default Arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Calling the function without providing a value for the 'greeting' parameter
result = greet("Boss")
print(result)  # Output: "Hello, Boss!"

# Calling the function and providing a custom value for the 'greeting' parameter
result_custom = greet("Boss", greeting="Good morning")
print(result_custom)  # Output: "Good morning, Boss!"
