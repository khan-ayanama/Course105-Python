# METHODS 

# isupper()
# The isupper() method returns True if all characters in the string are uppercase, and False otherwise:


uppercase_string = "HELLO, WORLD!"
mixed_case_string = "Hello, World!"

print(uppercase_string.isupper())  # True
print(mixed_case_string.isupper())  # False

# islower()
# The islower() method returns True if all characters in the string are lowercase, and False otherwise:


lowercase_string = "hello, world!"
mixed_case_string = "Hello, World!"

print(lowercase_string.islower())  # True
print(mixed_case_string.islower())  # False

# istitle()
# The istitle() method returns True if the string is titlecased (i.e., the first character of each word is uppercase, and the rest are lowercase), and False otherwise:


titlecased_string = "Hello World!"
mixed_case_string = "Hello, World!"

print(titlecased_string.istitle())  # True
print(mixed_case_string.istitle())  # False

# isdigit()
# The isdigit() method returns True if all characters in the string are digits (0-9), and the string is not empty. Otherwise, it returns False.


numeric_string = "12345"
non_numeric_string = "abc123"

print(numeric_string.isdigit())  # True
print(non_numeric_string.isdigit())  # False

# isalpha()
# The isalpha() method returns True if all characters in the string are alphabetic (letters), and the string is not empty. Otherwise, it returns False.


alphabetic_string = "abc"
alphanumeric_string = "abc123"

print(alphabetic_string.isalpha())  # True
print(alphanumeric_string.isalpha())  # False

# isalnum()
# The isalnum() method returns True if all characters in the string are alphanumeric (either letters or digits), and the string is not empty. Otherwise, it returns False.


alphanumeric_string = "abc123"
non_alphanumeric_string = "abc#123"

print(alphanumeric_string.isalnum())  # True
print(non_alphanumeric_string.isalnum())  # False

# isspace()
# isspace() method is used to check if all the characters in a string are whitespaces. 
whitespace_string = "    \t  \n"
non_whitespace_string = "Hello, World!"

print(whitespace_string.isspace())  # True
print(non_whitespace_string.isspace())  # False
