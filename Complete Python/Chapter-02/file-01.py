# Logical Operators
# Logical operators are used to connect more relational operation to form a complex expression called logical expression. A value obtained by evaluating a logica expression is always logical, i.e. either True or False

# AND
# (5<2) and (5>3) == False
True and True == True
True and False == True
False and True == True
False and False == True
True and 'Expression' == 'Expression'
False and 'Expression' == False
False and 'Expression1' and 'Expression2' == False
True and 'Expression1' and 'Expression2' == 'Expression2'

# OR Operator
True or True == True
True or False == True
False or True == True
False or False == True
True or 'Expression' == True
False or 'Expression' == 'Expression'
True or 'Expression1' or 'Expression2' == True
False or 'Expression1' or 'Expression2' == 'Expression1'

# not operator
False == True
True == False