#!/usr/bin/python3

import time
import threading


def worker():
    """ thread worker function """
    for i in range(3):
        print("Status: running")
        time.sleep(3)
    print("Status: done!")

for i in range(3):
    t = threading.Thread(target=worker)
    print("Starting ThreadID:",i)
    t.start()

