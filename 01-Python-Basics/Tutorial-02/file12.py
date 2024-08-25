# Number system in Python

# 1. Binary --> 0,1  (0B1011)
# 2. Decimal --> 0,1,2,...,9    (default)
# 3. Octal --> 0,1,2,...,8  (0o342)
# 4. Hexadecimal --> 0,1,2,...,0,a,b,c,d,e,f    (0x23ef)

decimal_number = 42
binary_representation = bin(decimal_number)
octal_representation = oct(decimal_number)
hexadecimal_representation = hex(decimal_number)

print(binary_representation)      # Output: '0b101010'
print(octal_representation)       # Output: '0o52'
print(hexadecimal_representation)  # Output: '0x2a'
