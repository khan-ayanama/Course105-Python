# date class
#creating object of date class
# obj_name = date(year,month,day)
# today(): returns current date

from datetime import date

d1 = date(year=2024,month=6,day=30)
print(d1)
print(d1.year)

d2 = date(2022,4,23)
print(d2)
print(date.today())