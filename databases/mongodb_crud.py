
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
        if data is not None:
            print("\n - ID:", data['_id'])
            print(" - Name:", data['Name'])
            print(" - Role:", data['Role'])
            print(" - CreateTime:", data['CreateTime'])
            print(" - UpdateTime:", data['UpdateTime'])
        else:
            print("No Record Was Found!")


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


    def delete_record(self):
        name = input("\nName: ")
        db = self.client.blog.Users
        data = db.remove({"Name": name})
        self.client.close()
        print(data)


    def delete_all_records(self):
        opt = input("\nDelete All Records (y/n)?")
        if opt == "y":
            db = self.client.blog.Users
            data = db.remove({})
            self.client.close()
            print("Done!")
        elif opt == "n":
            print("Aborted!")


database = Connector()

while True:
    print("\n\n=====> [MongoDB CRUD] <=====\n")
    options = [
                [1, "Create"],
                [2, "Read"],
                [3, "Update"],
                [4, "Delete"],
                [5, "Read All"],
                [6, "Delete ALl"],
                [0, "Exit"]
              ]
    for l in options:
        print(" - {0} ({1})".format(l[0],l[1]))

    opt = int(input("\n"))
    if opt == 1:
        print(database.create_record())
    elif opt == 2:
        database.read_record()
    elif opt == 4:
        database.delete_record()
    elif opt == 5:
        j = input("As JSON (y/n)?")
        if j == "y":
            database.read_all_records(True)
        else:
            database.read_all_records()
    elif opt == 6:
        database.delete_all_records()
    elif opt == 0:
        sys.exit(0)
