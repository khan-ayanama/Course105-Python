# Time Modules

# time(): It returns time in seconds since the epoch as floating point number.

# ctime(): It retunrns the current data and time when we pass epoch time to it.
# It returns date and time in string format, when we do not pass epoch time, it returns the current data and time in string format.

# localtime(): It converts seconds into date and time, It returns an object which can be accessed by either index or attributes.
# tm_year -> 4 digts year number
# tm_mon -> [1,31]
# tm_hour -> [0,23]
# tm_min -> [0,59]
# tm_sec -> [0,61]
# tm_zone -> Time zone