# Array module in python

# The array module in Python provides a way to create and work with arrays of a specific data type in a memory-efficient manner. It's particularly useful when you're dealing with large amounts of data and need to store and manipulate arrays of simple data types like integers or floats.

# Importing the Module:
from array import array

# 1. Creating an Array:
# 'i' specifies the data type (signed integer)
int_array = array("i", [1, 2, 3, 4, 5])

# You need to specify the type code that corresponds to the desired data type ('i' for signed integers in this example)


# Accessing Elements:
print(int_array[0])  # Accessing the first element

# Adding Elements:
int_array.append(6)  # Adding an element to the end

# Removing Elements:
int_array.remove(3)  # Removing an element (the first occurrence)

# Supported Data Types:
# The array module supports various type codes to represent different data types, such as integers, floats, and characters. Some common type codes include:
# 'b': signed char
# 'B': unsigned char
# 'i': signed int
# 'I': unsigned int
# 'f': float
# 'd': double


from array import array

# Creating arrays with different data types
int_array = array("i", [1, 2, 3])
float_array = array("f", [1.0, 2.5, 3.7])
char_array = array("b", [65, 66, 67])  # ASCII values of 'A', 'B', 'C'

print(int_array)
print(float_array)
print(char_array)

# the array module is more memory-efficient compared to lists when you're dealing with large datasets of a single data type. However, if you need more advanced array operations, consider using the NumPy library, which provides a more powerful and feature-rich array data structure called ndarray.
