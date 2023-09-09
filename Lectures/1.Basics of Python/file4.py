# Raw String

# Put 'r' before string to print exactly same escape sequence
print(r"line A \n line B")


print(r"line A \n line B'/\\")

# 1. Separation in print sep=":"

a = 10
b = 5
c = a+b
# print("value is ", a, b, sep=':')

# 2. end method
# This end method will remove the new line and next line will be in same line
print("value is ", a, b, sep=':', end='-----')

# 3. Format String
# %d, %i --> int
# %f --> float
# %s --> string

print("Addition of %d and %d is %d " % (a, b, c))



# How to code emoji
# At + use 000
# Use backslash initial of a UTF code

print("\U0001F602")
print("\U0001F600")


# Python as Calculator

# Float Division
print(2/4)

# Integer division
print(5//2)

# Exponent
print(2**3)

# Square Root
print(2**0.5)

# Rounding of a number
print(round(2**0.5, 2))
print(round(2.2342345, 3))  # Print after rounding three decimal places
