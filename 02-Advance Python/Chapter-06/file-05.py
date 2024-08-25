from datetime import datetime
dt1 = datetime(year=2019,month=6,day=30)
dt2 = datetime(year=2019,month=6,day=30,hour=15,minute=34)
dt3 = datetime(2017,4,28)

print(dt1)
print(dt1.year)
print(dt2)

# now(): current time
ct = datetime.now()
print(ct)
print(ct.day)

# today()
td = datetime.today()
print(td)
print(td.hour)