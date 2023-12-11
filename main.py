from dotenv import load_dotenv, find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.getenv("MONGODB_PWS")

connection_string = f"mongodb+srv://johnblessonrowe:{password}@tutorial.v5km3nl.mongodb.net/python-tutorial?retryWrites=true&w=majority"

client = MongoClient(connection_string)

dbs = client.list_database_names()
print(dbs)