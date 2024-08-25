# Typecasting (also known as type conversion) refers to the process of converting a variable from one data type to another.

# int()
num_str = "123"
num_int = int(num_str)
print(num_int)  # Output: 123

# float()
num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14

# str()
num_int = 42
num_str = str(num_int)
print(num_str)  # Output: "42"

# bool()
zero = 0
is_zero_true = bool(zero)
print(is_zero_true)  # Output: False

# list(), tuple(), set()
num_str = "123"
num_list = list(num_str)
print(num_list)  # Output: ['1', '2', '3']

# dict()
key_value_pairs = [("a", 1), ("b", 2)]
my_dict = dict(key_value_pairs)
print(my_dict)  # Output: {'a': 1, 'b': 2}

# Remember that not all type conversions are possible. For example, trying to convert a string that doesn't represent a valid number to an integer or float will result in an error.