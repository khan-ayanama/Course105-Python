# Functions intro

# Function for adding two numbers

def add_two(a, b):
    return a+b


print(add_two(2, 3))


# function inside function

def greater(a, b):
    if a > b:
        return a
    return b


def greatest(a, b, c):
    bigger = greater(a, b)
    return greater(bigger, c)


print(greatest(11, 5, 3))
