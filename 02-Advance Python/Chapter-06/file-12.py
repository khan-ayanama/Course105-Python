# Calculate Age
from datetime import date

dob = date(2000,10,15)
t = date.today()

age = t.year - dob.year -((t.month,t.day)<(dob.month,dob.day))
print(age)