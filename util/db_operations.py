import util.connection as con


# To drop a entire collection
def delete_collection(collection: str):
    dbname = con.get_database()
    return dbname[collection].drop()


# returns the first occurrence in the selection
def get_first_record(collection: str):
    dbname = con.get_database()
    return dbname[collection].find_one()


# Insert multiple document at once
def insert_multiple_document(collection, param):
    dbname = con.get_database()
    return dbname[collection].insert_many(param)


# to delete single record
def delete_single_document(collection, query):
    dbname = con.get_database()
    return dbname[collection].delete_one(query)


# To delete multiple document at once
def delete_multiple_document(collection, query):
    dbname = con.get_database()
    if query:
        return dbname[collection].delete_many(query)
    else:
        return dbname[collection].delete_many({})


# To select data from a collection in MongoDB, we can use the find_one() method.
# The find() method returns all occurrences in the selection.
# Return all documents or specific document in the "order_list" collection, and print each document:
def find_document(collection, query):
    dbname = con.get_database()
    if query:
        # Return Only Some Fields
        # The second parameter of the find() method is an object describing which fields to include in the result.
        # This parameter is optional, and if omitted, all fields will be included in the result.
        return dbname[collection].find(query)
    else:
        return dbname[collection].find()


def update_document(collection, query, value):
    dbname = con.get_database()
    return dbname[collection].update_one(query, value)
