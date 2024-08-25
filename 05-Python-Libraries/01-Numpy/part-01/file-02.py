# In numpy stores particular data type.
# You need to import numpy module


# Calculate time list vs numpy
import timeit as timeit

# List
timeit_result = timeit.timeit('[j**4 for j in range(1, 9)]', number=1000)
print(f"List comprehension time: {timeit_result} seconds")


# Array
setup_code = "import numpy as np"
timeit_result2 = timeit.timeit("np.arange(1, 9)**4", setup=setup_code, number=1000)
print(f"NumPy array time: {timeit_result2} seconds")
