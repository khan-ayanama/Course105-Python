# RESHAPE
# The numpy.reshape function is used to give a new shape to an existing array without changing its data. This function returns a new array with the same data but a different shape.
import numpy as np

# Create a 1-dimensional array
original_array = np.array([1, 2, 3, 4, 5, 6])

# Reshape the array to a 2x3 matrix
reshaped_array = np.reshape(original_array, (2, 3))

# Print the original and reshaped arrays
print("Original Array:")
print(original_array)

print("\nReshaped Array:")
print(reshaped_array)

# Output
# Original Array:
# [1 2 3 4 5 6]

# Reshaped Array:
# [[1 2 3]
#  [4 5 6]]

#  np.reshape(original_array, (2, 3)) reshapes the original 1-dimensional array into a 2x3 matrix. 


# the -1 in the second dimension of the reshaping tuple is a placeholder that tells NumPy to automatically infer the size of that dimension
reshaped_array_auto = np.reshape(original_array, (2, -1))
print("\nReshaped Array (Auto Dimension):")
print(reshaped_array_auto)


# FLATTEN
import numpy as np

# Create a 2-D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])

# Flatten the array
flattened_array = two_d_array.flatten()

# Print the original and flattened arrays
print("Original 2-D Array:")
print(two_d_array)

print("\nFlattened Array:")
print(flattened_array)

# The flatten function returns a new array, and modifying the flattened array does not affect the original array. If you want to modify the original array in place, you can use the ravel method:

flattened_array_ravel = two_d_array.ravel()

# Both flatten and ravel can be used to achieve a similar result, but ravel may return a view of the original array in certain cases, while flatten always returns a copy.