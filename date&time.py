#Date Time Module:-

import datetime as d
print(d.datetime.now())
print(d.date(2024,10,29))
date=d.date.today()
#print(date.year)
print(date.weekday())
anotherdate=d.timedelta(days=200)
nextday=date+anotherdate
print(date+anotherdate)
print(nextday)
print((nextday-date).days)



# time Module:-

time=d.time(10,50,43)
Dt=d.datetime.now()
print(time)
print(time.hour)
print(time.minute)
print(time.second)
print(Dt.strftime('%B'))
