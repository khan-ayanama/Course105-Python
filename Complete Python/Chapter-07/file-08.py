# strip

# strip()
# The strip() method removes leading and trailing whitespaces from a string. It returns a new string with whitespaces removed from both ends.

original_string = "   Hello, World!   "

# Using strip() to remove leading and trailing whitespaces
stripped_string = original_string.strip()

print("Stripped String:", stripped_string)

# lstrip()
# The lstrip() method removes leading whitespaces from a string. It returns a new string with whitespaces removed from the left side.


original_string = "   Hello, World!   "

# Using lstrip() to remove leading whitespaces
left_stripped_string = original_string.lstrip()

print("Left Stripped String:", left_stripped_string)

# rstrip()
# The rstrip() method removes trailing whitespaces from a string. It returns a new string with whitespaces removed from the right side.

original_string = "   Hello, World!   "

# Using rstrip() to remove trailing whitespaces
right_stripped_string = original_string.rstrip()

print("Right Stripped String:", right_stripped_string)