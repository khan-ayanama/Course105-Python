# Break
# The break statement is used to exit a loop prematurely, regardless of whether the loop condition is true or false.

for i in range(5):
    if i == 3:
        break
    print(i)

# Continue
# The continue statement is used to skip the rest of the code inside a loop for the current iteration and move to the next iteration.

for i in range(5):
    if i == 2:
        continue
    print(i)

# Pass
# The pass statement is a no-operation statement. It is used when a statement is syntactically required but you don't want any command or code to execute.
    
for i in range(5):
    if i == 2:
        pass
    else:
        print(i)