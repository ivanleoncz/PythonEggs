import datetime

now = datetime.datetime.now()
future = datetime.timedelta(minutes=15)
future_y = datetime.timedelta(days=730)

print("Time Now: ", now)
print("Time Now (no ms): ", now.replace(microsecond=0))
print("Time Future (15 min.): ", now + future)
print("Time Future (2 years.):", now + future_y)
print("Date: ", now.strftime('%d-%m-%Y'))
print("Time: ", now.strftime('%H:%M:%S'))
