
import datetime
import sys
from bson import json_util
from json import dumps
from pymongo import MongoClient

class Connector(object):

    def __init__(self):
        self.client = MongoClient('mongodb://mongo:mongo@127.0.0.1:27017')


    def create_record(self):
        name = input("\nName: ")
        role = input("Role: ")
        try:
            db = self.client.blog.Users
            record_id = db.insert(
                    {
                     "Name":name,
                     "Role":role,
                     "CreateTime":datetime.datetime.now(),
                     "UpdateTime":datetime.datetime.now()
                    }
            )
            self.client.close()
            return str(record_id)
        except Exception as e:
            return e


    def read_record(self):
        name = input("\nName: ")
        db = self.client.blog.Users
        data = db.find_one({"Name":name})
        self.client.close()
        print("\n - ID:", data['_id'])
        print(" - Name:", data['Name'])
        print(" - Role:", data['Role'])
        print(" - CreateTime:", data['CreateTime'])
        print(" - UpdateTime:", data['UpdateTime'])


    def read_all_records(self, dump=False):
        db = self.client.blog.Users
        data = db.find({})
        self.client.close()
        data = [record for record in data]
        if dump is False:
            for record in data:
                print(record)
        elif dump is True:
            print(dumps(data, indent=2, default=json_util.default))


database = Connector()

while True:
    print("\n\n=====> [MongoDB CRUD] <=====\n")
    options = [
                ["Create","c"],
                ["Read","r"],
                ["Update","u"],
                ["Delete","d"],
                ["Read All","a"],
                ["Exit","e"]
              ]
    for l in options:
        print(" - {0} ({1})".format(l[0],l[1]))
    opt = input("\n")
    if opt == "c":
        print(database.create_record())
    elif opt == "r":
        database.read_record()
    elif opt == "a":
        j = input("As JSON (y/n)?")
        if j == "y":
            database.read_all_records(True)
        else:
            database.read_all_records()
    elif opt == "e":
        sys.exit(0)
