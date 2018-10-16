#!/usr/bin/python3

import os
import subprocess as sp

env_vars = dict(os.environ)

create_file = ['echo', 'This is a message for:', env_vars["USER"]]

with open("/tmp/file.out", "w") as f:
    result = sp.call(create_file, stderr=sp.DEVNULL, stdout=f)
    if result == 0:
        print("Sucessfull!")
    else:
        print("Error while processing command.")
