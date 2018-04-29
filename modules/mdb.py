#!/usr/bin/python3


from bson.objectid import ObjectId
from datetime import datetime
from pymongo import MongoClient

__author__ = "@ivanleoncz"


class Connector:
    """  MongoDB Connector + Jobs. """
    
    def __init__(self, database, collection):
        """ Initializing database and collection data. """
        self.database = database
        self.collection = collection


    def connect(self):
        """ Configuring MongoDB client. """
        db_user = "mongo"
        db_pass = "mongo"
        db_addr = "127.0.0.1:27017"
        uri = "mongodb://{0}:{1}@{2}".format(db_user,db_pass,db_addr)
        client = MongoClient(uri,serverSelectionTimeoutMS=6000)
        return client


    def add(self, data):
        """ Adding record. """
        client = self.connect()
        db = client.self.database
        collection = db.self.collection
        result = collection.insert_one(data).inserted_id
        client.close()
        return result 


    def find(self, data):
        """ Verifying the existence of a specific record. """
        client = self.connect()
        db = client.self.database
        collection = db.self.collection
        result = collection.find({})
        client.close()
        for r in result:
            if data in str(r):
                print(r)


    def find_all(self):
        """ Displaying all information contained in a collection. """
        client = self.connect()
        db = client.self.database
        collection = db.self.collection
        result = collection.find({})
        client.close()
        for r in result:
            print(r)
