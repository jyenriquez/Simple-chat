import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta

# Creating information as a post

cluster = MongoClient("mongodb+srv://poporing:7sv7T7Vt0cPt@cluster0.tliy9.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

# Initializes the user database and collection
db = cluster["test"]
collection = db["users"]

# Initializing the message collection
collection_messages = db["messages"]

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

# Posts message into the DB
def post_message(message, user):
    post = {"name": user, "message": message, "dateAdded": datetime.today()}
    collection_messages.insert_one(post)

    # For debugging purposes
    # for document in cursor:
    #     print(document.get("message") + " - " +document.get("name"))

def get_messages():
    # Grabs all objects in collection_messages
    cursor = collection_messages.find({})
    return cursor
