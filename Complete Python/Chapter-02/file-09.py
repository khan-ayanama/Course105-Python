# Input Statements
# input(): This function is used to accept input from keyboard.
# This function will stop the program flow until the user gives an input and end the input with the return key
# Whatever user gives as input function convert it into a string. If user enters an integer value still input() function convert it into a string.
# So if you need an integer you have to use type conversion

# Syntax: input([pompt])
# prompt is a string or message, representing a default message before input. It is optional.

# Using input() with explicit type conversion
user_age_str = input("Enter your age: ")
user_age = int(user_age_str)  # Convert the entered string to an integer
print("You will be " + str(user_age + 1) + " years old next year.")

# boolean input
# Everything will be true except space even the False will be true because it will act as string which is true.
input_bool = bool(input("Enter the boolean"))
print(input_bool)
