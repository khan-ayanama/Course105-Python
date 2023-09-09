# List vs Array

# in list we can store any type of data-type
# python array-module -- fix data type
# numpy array - binding c
# javascritp array is almost same as python list


# list vs string

# strings are immutable
# lists are mutable

s = 'string'
s.title()  # does not change original string

l = ['word1', 'word2', 'word3']
l.pop()  # changes original list


# Looping in list

fruits = ['orange', 'apple', 'peawr', 'banana', 'kiwi']

# for loop
# for fruit in fruits:
#     print(fruit)

# while loop
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1


########### list inside list    ##########

matrix = [[2, 3, 1], [4, 5, 6], [7, 8, 9]]  # 2d list

# for sublist in matrix:
#     for i in sublist:
#         print(i)


ans = matrix[1][2]
print(ans)


# type of data
print(type(matrix))
