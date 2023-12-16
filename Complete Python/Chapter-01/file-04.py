# Variables

# Variables in C or Java
# In C, Java or some other programming langauges, a variable is an identifier or a name, connected to memory location
# For Example
# int a;  (Here a is intialized at some memory location)
# a = 5;  (Now value of that location is assigned as 5 at some other location as pointor)


# Variables in Python
# In python, a variable is considered as tag that is tied to some value, Python considers value as objects
# For Example:
# a = 5 (here value 5 is intialized and a is tag to that value not opposite as in python)

# Consider this example
a = 5
b = 5
print(id(a)) 
print(id(b))
# Here id which gives an address of that value will be same because 10 is assigned to some location and a and b is pointed to that location.



# Variable assignment
my_variable = 10

# Dynamic Typing:
my_variable = 10       # Integer
my_variable = "Hello"  # String

# Multiple Assignments:
a, b, c = 1, 2, 3

# Reassignment:
my_variable = 10
my_variable = my_variable + 5  # Reassignment

# Constants (by Convention):
MY_CONSTANT = 42

# Deleting Variables:
my_variable = 10
del my_variable
