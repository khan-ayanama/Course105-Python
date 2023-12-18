# Operator Precedence:

# Higher Precedence:
# Parentheses () have the highest precedence.
# Exponentiation ** has the next highest precedence.
# Multiplication *, Division /, Floor Division //, and Modulus % have the same precedence.
# Addition + and Subtraction - have the same precedence.

# Lower Precedence:
# Bitwise Shifts (<< and >>) have lower precedence.
# Bitwise AND & has lower precedence than shifts.
# Bitwise XOR ^ has lower precedence than AND.
# Bitwise OR | has the lowest precedence.

# Example:
result = 2 + 3 * 4
# Multiplication has higher precedence than addition, so it's evaluated first.
# Result: 14 (2 + (3 * 4))


# Operator Associativity:
# Left-to-Right:
# Most operators, including addition + and multiplication *, associate from left to right. 
# For example, a + b + c is evaluated as (a + b) + c.

# Right-to-Left:
# Exponentiation ** is right-associative. 
# For example, a ** b ** c is evaluated as a ** (b ** c).

# Example:
result_associativity = 2 ** 3 ** 2
# Exponentiation is right-associative, so it's evaluated from right to left.
# Result: 512 (2 ** (3 ** 2))

# Example 1: Operator Precedence
result = 2 + 3 * 4
# Multiplication has higher precedence than addition, so it's evaluated first.
# Result: 14 (2 + (3 * 4))

# Example 2: Operator Associativity
result_associativity = 2 ** 3 ** 2
# Exponentiation is right-associative, so it's evaluated from right to left.
# Result: 512 (2 ** (3 ** 2))
