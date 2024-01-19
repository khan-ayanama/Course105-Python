# Local varaibles

def example_function():
    # Local variable 'x' is defined within the function
    x = 10
    print("Inside the function:", x)

# Call the function
example_function()

# Attempting to access 'x' outside the function will result in an error
# Uncommenting the line below will raise a NameError
# print("Outside the function:", x)

# ------------------------------------------------
# Global Variable
# Global variable 'global_var' is defined outside any function
global_var = 5

def example_function():
    # Accessing the global variable 'global_var' within the function
    print("Inside the function:", global_var)

    # Modifying the global variable 'global_var'
    global global_var
    global_var = 10

# Call the function
example_function()

# Accessing the modified global variable 'global_var' outside the function
print("Outside the function:", global_var)
