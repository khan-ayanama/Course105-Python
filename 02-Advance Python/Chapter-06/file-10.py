# Formatting date and time
# strftime()

from datetime import datetime

dt = datetime.today()
print(dt)

print()

newd1 = dt.strftime("%B, %d, %Y")
print(newd1)
print()

newd2 = dt.strftime("%d/%b/ %Y")
print(newd2)
print()

newd3 = dt.strftime("%d-%m-%Y")
print(newd3)
print()

newd4 = dt.strftime("%H:%M:%Y")
print(newd4)
print()