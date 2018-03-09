#!/usr/bin/python3

"""  MongoDB utilities for PyCaptive. """

from bson.objectid import ObjectId
from datetime import datetime
from pymongo import MongoClient


class Connector:
    """ MongoDB connector and jobs: login, add session and delete session. """

    def connect(self):
        """ Configuring MongoDB client. """
        db_user = "mongo"
        db_pass = "mongo"
        db_addr = "127.0.0.1:27017"
        uri = "mongodb://{0}:{1}@{2}".format(db_user,db_pass,db_addr)
        client = MongoClient(uri,serverSelectionTimeoutMS=6000)
        return client


    def add_record(self):
        """ Adding record. """
        client = self.connect()
        db = client.new_database
        collection = db.new_collection
        result = collection.insert_one({"Username":"alan.turing","Country":"England",
                                "Birthdate":"06-23-1912","Died":"06-07-1954",
                                "Record":datetime.now()})
        data = self.find_record(result.inserted_id)
        return data


    def find_record(self, obj_id):
        """ Verifying existence object ID. """
        client = self.connect()
        db = client.new_database
        collection = db.new_collection
        result = collection.find_one({"_id":ObjectId(obj_id)})
        return result


if __name__ == "__main__":
    db = Connector()
    result = db.add_record()
    if len(result) != 0:
        print("Record successfully added!")
    else:
        print("Record not found!")



