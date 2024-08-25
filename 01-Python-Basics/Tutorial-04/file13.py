# Modules in python

#  In Python, a module is a file containing Python definitions and statements. The file name is the module name with the suffix .py. Modules allow you to organize your code into separate files, making it easier to manage and reuse code across different projects.


# Creating a Module:
# To create a module, you simply create a .py file with your Python code. For example, if you create a file named my_module.py, you can import and use it in other scripts.


# Importing a Module:
# You can import a module using the import statement. For example, if you have a module named my_module.py, you can import it like this:

# import my_module

# You can then access the functions, classes, and variables defined in my_module using dot notation, like my_module.my_function().


# Renaming a Module:
# You can give a module a shorter alias when importing it, which can make your code more concise:

# import my_module as mm


# Importing Specific Items:
# You can import specific items from a module:

# from my_module import my_function, my_variable


# The if __name__ == "__main__": Block:
# This block is often used in Python scripts. It ensures that the code inside it is only executed when the script is run directly, not when it's imported as a module. It's useful for testing and running scripts.

# def my_function():
#     # ...

# if __name__ == "__main__":
#     # This code will only run when the script is executed directly
#     my_function()


# Built-in Modules:
# Python comes with a wide range of built-in modules that provide additional functionality, such as math, random, datetime, and more. You can use these modules to perform various tasks without having to reinvent the wheel.