# Conditional Statements

# If statement
# In Python, an if statement is used for conditional execution. It allows you to execute a block of code only if a specified condition is true. Here's the basic syntax:

x = 5
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")



# If with logical operators
# Example
x = 10
y = 5

if x > 0 and y > 0:
    print("Both x and y are positive")

if x > 0 or y > 0:
    print("At least one of x or y is positive")

if not x < 0:
    print("x is not negative")

# Example:
if (x > 0 and y > 0) or (x == 0 and y == 0):
    print("Either both x and y are positive or both are zero")
