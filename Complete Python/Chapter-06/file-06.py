# INPUT in numpy array
# When you want to get input from a user and create a NumPy array, you can use the numpy.array function along with the input function in Python. Here's a simple example:
import numpy as np

# Get the elements of the array from the user
user_input = [float(x) for x in input("Enter elements separated by space: ").split()]

# Create a NumPy array from the user input
numpy_array = np.array(user_input)

# Print the resulting NumPy array
print("\nNumPy Array:")
print(numpy_array)
