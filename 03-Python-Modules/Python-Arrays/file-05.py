# Gettin an array input from using for loop in Python

# Example:
from array import *
student_roll = array('i',[])

n = int(input("How many elements?"))
for i in range(n):
    student_roll.append(int(input("Enter Element:")))
for i in range(len(student_roll)):
    print(student_roll[i])
