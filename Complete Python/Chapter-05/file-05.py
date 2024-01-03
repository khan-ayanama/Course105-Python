# linspace() Function

# linspace(): It is used to create an array with evenely spaced numbers between a starting and stoping point

# Syntax:
# numpy.linspace(start,num=50,endpoint=True,retstep=False,dteype=None,axis=0)
# start: represents starting point
# stop: represents ending point
# num: represents number of parts the element should be divided. Default is 50
# endpoint: If True, stop is the last element. If false, stop is not included

# The linspace function generates evenly spaced values over a specified range. Here's an example:

import numpy as np

# Creating a one-dimensional array using linspace
import numpy as np

# Creating a one-dimensional array using linspace
arr = np.linspace(start=1, stop=5, num=10)

print("Generated Array:")
print(arr)

# Generated Array:
# [1.         1.44444444 1.88888889 2.33333333 2.77777778 3.22222222
#  3.66666665
# 7 4.11111111 4.55555556 5.        ]
