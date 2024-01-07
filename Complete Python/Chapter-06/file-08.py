# Accessing Numpy Two Dimensional Array using for Loop in Python 

import numpy as np

# Create a 2-D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Access elements using a for loop
for row in range(two_d_array.shape[0]):  # Iterate over rows
    for col in range(two_d_array.shape[1]):  # Iterate over columns
        print(f"Element at ({row}, {col}): {two_d_array[row, col]}")

# Accessing Numpy Two Dimensional Array using for While in Python 
# Create a 2-D array
two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Get the shape of the array
rows, cols = two_d_array.shape

# Initialize row and column counters
row = 0

while row < rows:
    col = 0
    while col < cols:
        print(f"Element at ({row}, {col}): {two_d_array[row, col]}")
        col += 1
    row += 1
