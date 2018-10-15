#!/usr/bin/python3

# https://docs.python.org/3.5/howto/logging.html

import logging

logging.basicConfig(filename='logging_to_file.log',
                    format='%(asctime)s %(message)s',
                    level=logging.INFO)

name = input("Name: ")
if name is "":
    logging.warning("No Name was provided.")
else:
    logging.info("Name has been informed: %s", name)
country = input("Country: ")
logging.info("Country has been informed: %s", country)
birthdate = input("Birthdate: ")
logging.info("Birthdate has been informed: %s", birthdate)
