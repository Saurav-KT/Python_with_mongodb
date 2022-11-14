from datetime import datetime
import json

import util.connection as con
import util.db_operations as operations

new_posts = [{"author": "Saurav",
              "text": "MongoDB with python series",
              "address": "Bangalore",
              "tags": ["bulk", "insert"]},
             {"author": "Raghaw",
              "address": "Delhi",
              "title": "fun at work",
              "text": "and pretty easy too!"}]

# Return all documents in the "order_list" collection, and print each document:
# for item in operations.return_all("order_list"):
#     print(item)

# Return Only Some Fields
# The second parameter of the find() method is an object describing which fields to include in the result.
# for item in collection_name.find({"author": "Mike"}):
#     print(item)

# To insert multiple document
operations.insert_multiple_document("order_list", new_posts)

# to update specific document
myquery = {"author": "Saurav"}
newvalues = {"$set": {"postal code": "560110"}}
x = operations.update_document("order_list", myquery, newvalues)
print(x.modified_count)

# To Delete the single document with the author: saurav
# query = {"author": "Saurav"}
# print(operations.delete_single_document("order_list", query))

# To Delete more than one document.
# query = {"author": {"$regex": "^Saurav"}}
# print(operations.delete_multiple_document("order_list", None))

# x = operations.delete_multiple_document("order_list")
# print(x.deleted_count, "documents deleted")

# query = {"author": "Priya"}
# operations.find_document("order_list",)
