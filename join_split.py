#!/usr/bin/python3
""" Demonstrates the usage of the built-ins join() and split()."""

__author__ = "@ivanleoncz"

server_conf = {"ServerType":"Proxy", "Country":"JAP", "OS":"Debian"}

for k,v in server_conf.items():
    string = "=".join([k,v])
    print(string)
    print(string.split("="),"\n")


