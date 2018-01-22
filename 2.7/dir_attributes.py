#!/usr/bin/python
""" Demonstrates the usage of dir(), with better output. """

__author__ = "ivanleoncz"

obj = "I am a string."
count = 0

print "\nObject Data: %s" % obj
print "Object Type: %s\n" % type(obj)

for method in dir(obj):
    # the comma at the end of the print, makes it printing 
    # in the same line, 4 times (count)
    print "| {0: <20}".format(method),
    count += 1
    if count == 4:
        count = 0
        print 
