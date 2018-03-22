#!/usr/bin/python3

import json
import whois

data = str(whois.whois("stackoverflow.com"))
info = json.loads(data)
print("Company:", info["org"])
