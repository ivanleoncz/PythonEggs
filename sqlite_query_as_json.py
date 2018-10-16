#!/usr/bin/python3

""" Demonstrating SQLite3 query with data returned as JSON Array. """

from json import dumps                                                          

__author__ = "@ivanleoncz"

import sqlite3                                                                  
                                                                                
def data_as_json():                                                                 
    db = sqlite3.connect("app_db.sqlite3")                                       
    cursor = db.cursor()                                                        
    query = """ SELECT * FROM Users """                                       
    cursor.execute(query)                                                       
    data = [ row for row in cursor.fetchall() ]                                 
    db.commit()                                                                 
    return dumps(data, indent=4)                                                
                                                                                
print(data_as_json())
