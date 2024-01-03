# logspace() Function
# The logspace function generates numbers spaced evenly on a log scale. Here's an example:

import numpy as np

# Creating a one-dimensional array using logspace
arr = np.logspace(start=1, stop=5, num=10, base=10)

print("Generated Array:")
print(arr)

# start is the starting power of the sequence, stop is the ending power, num is the number of samples to generate, and base is the base of the logarithm.