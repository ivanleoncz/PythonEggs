
import datetime

DIFFERENCE=3600

time_now = datetime.datetime.now()
time_future = time_now + datetime.timedelta(seconds=DIFFERENCE)

print("Time Now:              ", time_now)
print("Time Future:           ", time_future)
print("Time Difference (sec.):", DIFFERENCE)
