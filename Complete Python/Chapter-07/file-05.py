# FORMATTING STRING

# C STYLE FORMATTING
# C-style formatting for strings using the % operator. This style of string formatting is similar to the one used in the C programming language. The basic syntax involves using the % operator to replace placeholders in a string with values.

# %s: String (or any object with a string representation)
# %d: Integer
# %f: Floating-point number
# %x: Hexadecimal integer
name = "John"
age = 30

# C-style string formatting
formatted_string = "My name is %s and I am %d years old." % (name, age)

print(formatted_string)


# format()
# format() method in Python is a versatile and powerful way to format strings. It allows you to insert values into a string in a flexible manner. The basic syntax involves creating a string with placeholders (using curly braces {}), and then using the format() method to replace the placeholders with values.

name = "John"
age = 30

# Using the format() method
formatted_string = "My name is {} and I am {} years old.".format(name, age)

print(formatted_string)


# f-string
name = "John"
age = 30

# Using f-string
formatted_string = f"My name is {name} and I am {age} years old."

print(formatted_string)
