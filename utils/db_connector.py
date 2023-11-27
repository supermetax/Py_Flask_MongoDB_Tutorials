from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''
Function : Connecting to the Mongo DB 
'''
# Access MongoDB URI from environment variables
mongo_uri = os.getenv('MONGODB_URI')
mongo_db_name = os.getenv('MONGODB_DBNAME_01')
mongo_collection_name = os.getenv('MONGODB_COLLECTION_01')

def connect_to_mongodb():
    try:
        # Create a MongoClient
        client = MongoClient(mongo_uri)
        db = client[mongo_db_name]
        collection = db[mongo_collection_name]
        return collection

    except Exception as e:
        print(f'Error connecting to MongoDB: {e}')
        return None