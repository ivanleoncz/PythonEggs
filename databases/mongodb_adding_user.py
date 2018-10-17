#!/usr/bin/python3

from json import dumps
from pymongo import MongoClient


client = MongoClient('mongodb://mongo:mongo@127.0.0.1', 27017)

db = client['blog']
collection = db['users']

user_data = {}
user_data["FullName"]  = input("- User Name:  ")
user_data["BirthDate"] = input("- Birth Date: ")
user_data["Country"]   = input("- Country:    ")
user_data["UserName"]  = input("- User Name:  ")
user_data["PassWord"]  = input("- Password:   ")


print(dumps(user_data, indent=4))

confirm = input("\nAdd record to database (y/n)? ")
if confirm == "y" or confirm == "Y":
    record = collection.insert_one(user_data).inserted_id
    client.close()
    print(record)
else:
    client.close()
    print("Interrupted!")
