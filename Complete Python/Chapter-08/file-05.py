# Variable Length Argument
# It strores all values in tuples

# *args
def sum_all(*args):
    total = sum(args)
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15


# **kwargs
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Boss", age=30, role="Manager")
