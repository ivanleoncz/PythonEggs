#!/usr/bin/python3

import os
import subprocess as sp
import sys

if os.getuid() != 0:
    print("Must be executed by root user!")
    sys.exit(2)

if not os.path.isfile('/sbin/iptables'):
    print("No iptables binary was found!")
    sys.exit(2)
try:
    loop = 0
    while loop == 0:
        sp.call(['clear'])
        print("<Iptables Worker>\n")
        print("1. Add\n2. Del\n3. List\n4. Exit\n\n")
        opt = input("Option: ")
        if opt == "1":
            print("Addind...\n")
            r = sp.call(['/sbin/iptables','-A','INPUT','-i','lo','-s','127.0.0.1','-p','tcp','--dport','10800','-j','DROP'])
            if r == 0:
                print("Successful!")
            else:
                print("Fail!")
            input("Press any key...\n")
        elif opt == "2":
            print("Deleting...\n")
            r = sp.call(['/sbin/iptables','-D','INPUT','-i','lo','-s','127.0.0.1','-p','tcp','--dport','10800','-j','DROP'])
            if r == 0:
                print("Successful!")
            else:
                print("Fail!")
            input("Press any key...\n")
        elif opt == "3":    
            print("Listing...\n")
            p = sp.Popen('/sbin/iptables -nvL | grep 10800', shell=True, stdout=sp.PIPE)
            output = p.stdout.read()
            if len(output) == 0:
                print("Not Found!\n")
            else:
                print(output.decode('utf-8'))
            input("Press any key...\n")
        elif opt == "4":
            loop = 1
            print("\nBye!\n")
        else:
            print("Wrong Option!\n")
            input("Press any key...\n")
except KeyboardInterrupt:
    print("\nInterrupted!\n")

