# Accesing array using for loop array module in python

from array import *

student_roll = array('i',[1,2,3,4,5])

# Without Index
for eleement in student_roll:
    print(eleement)

# With Index
for i in range(len(student_roll)):
    print(student_roll[i])

# Accesing Array using while loop
i = 0
while(i<len(student_roll)):
    print(student_roll[i])
    i+=1