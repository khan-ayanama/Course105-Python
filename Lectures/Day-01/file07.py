# User input
# input in integer
# num = int(input("Enter a number "))
# print("this is number " + str(num))

# Input in float
# num1 = float(input("Enter floating point number "))
# print(num1)

# input in bool
# Any input in bool in python is true only empty value consider as false
is_bool = bool(input("Enter true or false "))
if is_bool == 1:
    print("True")
else:
    print("False")

print(1 == 2)


# Waiting for the User
# input("\n\nPress the enter key to exit.")
# print("New line")

# 5.Multiple statement in single line
# name = 'Ayan';print(name.upper())

# Two or more input in one line

# name, age = input("Enter your name and age ").split(",")
last_name, old_age = input("Enter your last_name and old_age ").split()
# print(name)
# print(age)
print(last_name)
print(old_age)
