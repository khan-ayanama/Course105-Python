# Global Keyword
global_var = 5  # This is a global variable

def example_function():
    # Accessing the global variable 'global_var'
    print("Inside the function (before modification):", global_var)

    # Modifying the global variable using the 'global' keyword
    global global_var
    global_var = 10

    # Accessing the modified global variable 'global_var'
    print("Inside the function (after modification):", global_var)

# Call the function
example_function()

# Accessing the modified global variable 'global_var' outside the function
print("Outside the function:", global_var)
