
from pymongo import MongoClient

class Connector(object):

    def __init__(self):
        self.client = MongoClient('mongodb://mongo:mongo@127.0.0.1:27017')

    def add_record(self):
        name = input("Name: ")
        role = input("Role: ")
        try:
            db = self.client.blog.Users
            db.insert_one({"Name":name, "Role":role})
            self.client.close()
            return "Done!"
        except Exception as e:
            return e

    def search_record(self):
        name = input("Name: ")
        db = self.client.blog.Users
        data = db.find_one({"Name":name})
        self.client.close()
        return data


