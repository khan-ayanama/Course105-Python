from time import time, ctime, localtime

# time()
epoch = time()
print(epoch)

# ctime(epoch)
et = ctime(epoch)
print(et)
print(ctime())

# localtime
time_obj = localtime()
print(time_obj)
print(time_obj.tm_hour)


# Printing data
print(time_obj.tm_mday,end='/')
print(time_obj.tm_mon,end='/')
print(time_obj.tm_year)

# Printing time
print(time_obj.tm_hour,end=":")
print(time_obj.tm_min,end=":")
print(time_obj.tm_sec,end=":")