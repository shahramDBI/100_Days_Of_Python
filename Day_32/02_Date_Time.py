import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
week = now.weekday()
time = now.time()
hour = now.hour
minute = now.minute
second = now.second
print(now)
print(year)
print(month)
print(day)
print(week)
print(time)
print(hour)
print(minute)
print(second)

date_of_birth = dt.datetime(year=1979, month=11, day=1, hour=13, minute=16)
print(f"My birthday is: {date_of_birth}")
