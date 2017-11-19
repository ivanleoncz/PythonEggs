#!/usr/bin/python3

from datetime import datetime,timedelta
from time import sleep

sec = input("\nNumber os seconds (ex: 20): ")

present = datetime.now()
future = present + timedelta(seconds=int(sec))
present = str(present).split(".")[0]
future = str(future).split(".")[0]

print("\nStart:  ", present)
print("Finish: ", future)

stop = False
while stop == False:
    present = str(datetime.now()).split(".")[0]
    if present != future:
        print("Not ready...")
        sleep(1)
    else:
        print("Ready! ", present)
        stop = True

