# Range Function
# range(stop)
# range(start, stop)
# range(start, stop, step)

# Example 1: Using only the stop parameter
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Example 2: Using start and stop parameters
for i in range(2, 8):
    print(i)

# Output:
# 2
# 3
# 4
# 5
# 6
# 7

# Example 3: Using all three parameters (start, stop, step)
for i in range(1, 10, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9

my_list = list(range(5))
print(my_list)
# Output: [0, 1, 2, 3, 4]
