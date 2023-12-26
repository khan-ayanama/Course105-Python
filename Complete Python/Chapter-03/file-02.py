# Indentation
# Indentation is crucial in Python, Boss! Unlike many other programming languages that use braces {} to define blocks of code, Python uses indentation. The level of indentation determines the grouping of statements. Here's an example:


if True:
    print("This is indented")  # This line is indented, and it belongs to the if block
    print("So is this")         # This line is also part of the if block

print("This is not indented")   # This line is not indented, so it's not part of the if block

x=y=4
if x > 0:
    print("x is positive")  # 4 spaces used for indentation
    if y > 0:
        print("y is also positive")  # 8 spaces used for indentation within the nested if block


# if elif else statement       
x = 10

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")
