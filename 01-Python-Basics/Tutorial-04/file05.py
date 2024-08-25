# *args with normal parameter

# when normal arguement you have to pass the parameter otherwise it will give an error
def multiply_nums(num, *args):
    print(num)
    mul = 1
    for i in args:
        mul *= i
    return mul


# here first argument will be assigned to num and rest to the args in the form of tuple
print(multiply_nums(2, 3, 3, 4, 5))


# Args as argument

# def multiply_nums(*args):
#     mul = 1
#     for i in args:
#         mul *= i
#     return mul


# nums = [1, 2, 3, 4]
# print(multiply_nums(*nums))  # *nums will unpack nums


# ##############    HW  ############

# power of elements to num in function

def to_power(num, *args):
    if args:
        return [i**num for i in args]
    else:
        return "You didn't pass any args"


nums = [1, 2, 3]
print(to_power(2, *nums))
