# timedelta obj -> duration

from datetime import timedelta,date

td = timedelta(days=10)
d = date.today()

# Future Date after td day
print(d+td)
print(d-td)
