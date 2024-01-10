# FUNCTIONS
def print_name(name):
    print("Your name is ",name)

print_name('Ayan Khan')


# Returning single value
def add_numbers(a, b):
    result = a + b
    return result

# Using the function
sum_result = add_numbers(3, 4)
print(sum_result)  # Output: 7


# Returning multiple values
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Using the function
numbers_list = [1, 2, 3, 4, 5]
total_result, average_result = calculate_stats(numbers_list)
print(f"Total: {total_result}, Average: {average_result}")
# Output: Total: 15, Average: 3.0


# Returning a variable number of values
def get_values(*args):
    return args

# Using the function
result = get_values(1, 2, 3, 4, 5)
print(result)  # Output: (1, 2, 3, 4, 5)
