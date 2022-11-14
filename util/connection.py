from pymongo import MongoClient


def get_database():
    # CONNECTION_STRING = "mongodb+srv://user:pass@cluster.mongodb.net/myFirstDatabase"
    connection = MongoClient("mongodb://localhost:27017/")
    db = connection["user_shopping_list"]
    return db





