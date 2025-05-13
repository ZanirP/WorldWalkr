from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

ATLAS_URI = os.getenv("ATLAS_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

class AtlasClient:
    
    def __init__(self, atlas_uri, db_name):
        self.mongodb_client = MongoClient(atlas_uri)
        self.database = self.mongodb_client[db_name]
        
    # ping is used to check if the connection to the database is successful
    def ping(self):
        self.mongodb_client.admin.command('ping')
        
    # Get the MongoDB Atlas collection to connect to
    def get_collection(self, collection_name):
        collection = self.database[collection_name]
        return collection
    
    # Query the MongoDB Atlas collection
    def find(self, collection_name, filter={}, limit=0):
        collection = self.database[collection_name]
        items = list(collection.find(filter=filter, limit=limit))
        return items
    
    

atlas_client = AtlasClient(ATLAS_URI, DB_NAME)
atlas_client.ping()
print("Connected to Atlas instance! We are good to go!")