# time object -> Object containing info about local time
# obj_name = time(hour, min, s, mics,tzinfo)

from datetime import time

t = time(hour=15,minute=34,second=12)
print(t)
print(t.hour)

t2 = time(13,44,55)
print(t2)