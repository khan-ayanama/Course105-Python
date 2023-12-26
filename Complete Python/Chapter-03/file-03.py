# While Loop
count = 0

while count < 5:
    print("Count:", count)
    count += 1

# Nested while loop
row = 0

while row < 3:
    col = 0
    while col < 3:
        print(f"({row}, {col})", end=" ")
        col += 1
    print()  # Move to the next line after each row
    row += 1
