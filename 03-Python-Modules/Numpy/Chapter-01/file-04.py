# numpy array with for loop

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Accessing elements using a for loop
for element in arr:
    print(element)


# Accessing elements using a for loop with indexing
for i in range(len(arr)):
    element = arr[i]
    print(f"Element at index {i}: {element}")


# Accessing elements using a while loop with indexing
i = 0
while i < len(arr):
    element = arr[i]
    print(f"Element at index {i}: {element}")
    i += 1
