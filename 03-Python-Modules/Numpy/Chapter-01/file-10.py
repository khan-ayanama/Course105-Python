import numpy as np

# Creating two one-dimensional arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Addition
result_addition = arr1 + arr2
print("Addition:", result_addition)

# Subtraction
result_subtraction = arr1 - arr2
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = arr1 * arr2
print("Multiplication:", result_multiplication)

# Division
result_division = arr1 / arr2
print("Division:", result_division)

# Element-wise square root
result_sqrt = np.sqrt(arr1)
print("Square Root of arr1:", result_sqrt)

# output:
# Addition: [ 7  9 11 13 15]
# Subtraction: [-5 -5 -5 -5 -5]
# Multiplication: [ 6 14 24 36 50]
# Division: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
# Square Root of arr1: [1.         1.41421356 1.73205081 2.         2.23606798]


# Comparing numpy arrays
# Comparing arrays should be of the same size
# Creating two one-dimensional arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 2, 8, 4, 10])

# Element-wise comparison
elementwise_comparison = arr1 == arr2
print("Element-wise Comparison:", elementwise_comparison)

# Check if all elements are equal
all_elements_equal = np.array_equal(arr1, arr2)
print("All Elements Equal:", all_elements_equal)

# Check if any element is equal
any_element_equal = np.any(arr1 == arr2)
print("Any Element Equal:", any_element_equal)

# Check if arrays are equal (element-wise and shape-wise)
arrays_equal = np.array_equal(arr1, arr2)
print("Arrays Equal:", arrays_equal)

# output
# Element-wise Comparison: [False  True False  True False]
# All Elements Equal: False
# Any Element Equal: True
# Arrays Equal: False
