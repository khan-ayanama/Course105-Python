# Implicit Type Conversion
# Implicit type conversion, also known as automatic type conversion, occurs automatically when Python converts one data type to another without the programmer's intervention. This is done to accommodate the operation being performed.

# Implicit conversion from int to float
x = 5
y = 2.0
result = x + y
print(result)  # Output: 7.0 (int is implicitly converted to float)

# Explicit Type Conversion (Type Casting):
# Explicit type conversion, also known as type casting or type coercion, is done by the programmer using built-in functions to convert one data type to another.

# Explicit conversion from float to int
a = 7.8
b = int(a)
print(b)  # Output: 7 (float is explicitly converted to int)

# Explicit Type Conversion (Type Casting) Examples:

# Converts to an integer
int_value = int(5.7)
print(int_value)  # Output: 5

# Converts to a floating-point number
float_value = float(7)
print(float_value)  # Output: 7.0

# Converts to a string
str_value = str(123)
print(str_value)  # Output: '123'

# Converts to a boolean
bool_value = bool(0)
print(bool_value)  # Output: False
