import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta

# Creating information as a post

cluster = MongoClient("mongodb+srv://poporing:7sv7T7Vt0cPt@cluster0.tliy9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Initializes the database
db = cluster["test"]
collection = db["test"]

def post_name(name):
    post = {"name": name, "dateAdded": datetime.today()}
    collection.insert_one(post)


