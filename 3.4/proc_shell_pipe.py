#!/usr/bin/python3

import subprocess as sp

p = sp.Popen("df -hPT | grep boot", shell=True, stdout=sp.PIPE)

output = p.stdout.read()
print(output.decode('utf-8'))
