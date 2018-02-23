#!/usr/bin/python3

""" Demonstration of Firewall rules management for IPTABLES/Netfilter. """

__version__ = "1.0"
__author__  = "ivanleoncz"


import os
import subprocess as sp
import sys


def worker_add():
    r = sp.call(['/sbin/iptables',
                 '-A','INPUT','-i','lo','-s','127.0.0.1',
                 '-p','tcp','--dport','10800','-j','DROP'])
    if r == 0:
        return "Successful!\n"
    else:
        return "Fail!\n"


def worker_del():
    r = sp.call(['/sbin/iptables',
                 '-D','INPUT','-i','lo','-s','127.0.0.1',
                 '-p','tcp','--dport','10800','-j','DROP'])
    if r == 0:
        return "Successful!\n"
    else:
        return "Fail!\n"


def worker_list():
    p = sp.Popen('/sbin/iptables -nvL | grep 10800', shell=True, stdout=sp.PIPE)
    output = p.stdout.read()
    if len(output) == 0:
        return "Not Found!\n"
    else:
        return output.decode('utf-8')


if __name__ == "__main__":
    # the script can only be executed by root
    if os.getuid() != 0:
        print("Must be executed by root user!")
        sys.exit(2)
    # iptables binary must be present
    if not os.path.isfile('/sbin/iptables'):
        print("No iptables binary was found!")
        sys.exit(2)
    while True:
        sp.call(['clear'])
        print("\n[Iptables Worker]")
        opt = input("\n1. Add\n2. Del\n3. List\n4. Exit\n\nOption: ")
        if opt == "1":
            print(worker_add())
            input("Press any key...\n")
        elif opt == "2":
            print(worker_del())
            input("Press any key...\n")
        elif opt == "3":
            print(worker_list())
            input("Press any key...\n")
        elif opt == "4":
            input("Bye!\n")
            break
        else:
            input("Wrong Option! Press any key...\n")
