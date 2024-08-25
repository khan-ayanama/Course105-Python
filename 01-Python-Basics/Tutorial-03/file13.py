# Bytes and Bytearray in

# This type of data usually use in where you want to transfer data 1byte at a time like video streaming services

# BYTES
# The bytes data type represents an immutable sequence of bytes.
# It is an immutable sequence of integers in the range 0 to 255.
# Once a bytes object is created, its contents cannot be changed.
# The typical way to create a bytes object is by using the b prefix with a string literal that contains ASCII characters or using the bytes() constructor with an iterable of integers.

# Using a string literal with the 'b' prefix
my_bytes = b'Hello, World!'

# Using the bytes() constructor with an iterable of integers
my_bytes = bytes([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])

############################################################


# BYTEARRAY

# The bytearray data type represents a mutable sequence of bytes.
# It is similar to the bytes type, but unlike bytes, a bytearray object can be modified after creation.
# The elements of a bytearray are also integers in the range 0 to 255.
# You can create a bytearray using the bytearray() constructor with an iterable of integers or by converting an existing bytes object to a bytearray using the bytearray() constructor.


# Using the bytearray() constructor with an iterable of integers
my_bytearray = bytearray(
    [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])

# Modifying a bytearray
my_bytearray[0] = 104  # Changing 'H' to 'h'
my_bytearray.append(63)  # Appending '?' to the end
