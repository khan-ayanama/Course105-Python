# Default parameters

def user_info(first_name='unknown', last_name='unknown', age=None):
    print(f"your first name is {first_name}")
    print(f"your last name is {last_name}")
    print(f"your age is {age}")


# user_info('Ayan', 'khan', 20)
user_info()


# Variable Scope

# value of x is contained in the function
# def func():
#     x = 7
#     return x

# you can't access the x because it is locable varible to func function
# print(x)
