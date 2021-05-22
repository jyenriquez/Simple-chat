import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta

# Creating information as a post

cluster = MongoClient("mongodb+srv://poporing:7sv7T7Vt0cPt@cluster0.tliy9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Initializes the database
db = cluster["test"]
collection = db["test"]

# Posts a new name to the DB
def post_name(name):
    if get_name(name) is True:
        return
    post = {"name": name, "dateAdded": datetime.today()}
    collection.insert_one(post)

# Gets user only by the name
def get_name(name):
    found_name = collection.find_one({"name": name})
    if found_name is None:
        return False
    return True


