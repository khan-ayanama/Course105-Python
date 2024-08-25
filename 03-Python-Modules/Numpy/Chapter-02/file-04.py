# Aliasing Array
# Aliasing means giving another name to existing object. It doesn't mean copying.

import numpy as np

# Creating an array
original_array = np.array([1, 2, 3, 4, 5])

# Creating an alias by assigning a new name to the original array
alias_array = original_array

# Modifying the alias will also modify the original array
alias_array[0] = 99

# Printing both arrays
print("Original Array:", original_array)
print("Alias Array:", alias_array)


# COPYING AN ARRAY

# Creating an array
original_array = np.array([1, 2, 3, 4, 5])

# Creating a true copy of the array
copied_array = original_array.copy()

# Modifying the copied array will not affect the original array
copied_array[0] = 99

# Printing both arrays
print("Original Array:", original_array)
print("Copied Array:", copied_array)
