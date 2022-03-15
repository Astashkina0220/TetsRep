import datetime
now = datetime.datetime.now()
today = now.date()
moment = now.time()

print(now) # datetime.datetime(2017, 4, 14, 16, 38, 46, 271475)
print(today) # datetime.date(2017, 4, 14)
print(moment) # datetime.time(16, 38, 46, 271475)