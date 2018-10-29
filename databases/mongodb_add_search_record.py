
from bson import json_util
from json import dumps
from pymongo import MongoClient

class Connector(object):

    def __init__(self):
        self.client = MongoClient('mongodb://mongo:mongo@127.0.0.1:27017')

    def add_record(self):
        name = input("Name: ")
        role = input("Role: ")
        try:
            db = self.client.blog.Users
            record_id = db.insert({"Name":name, "Role":role})
            self.client.close()
            return str(record_id)
        except Exception as e:
            return e

    def search_record(self):
        name = input("Name: ")
        db = self.client.blog.Users
        data = db.find_one({"Name":name})
        self.client.close()
        return data


    def dump_records(self):
        db = self.client.blog.Users
        data = db.find({})
        data = [record for record in data]
        self.client.close()
        return dumps(data, indent=2, default=json_util.default)


database = Connector()
print(database.dump_records())
