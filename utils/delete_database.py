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

'''
Function : To delete/ drop the database
'''
def drop_collection():
    try:
        # Connect to MongoDB
        collection = connect_to_mongodb()

        if collection:
            # Drop the specified collection
            collection.drop()

            print(f'Collection {collection} dropped successfully.')
        else:
            print("Unable to connect to MongoDB. Check your connection details.")

    except Exception as e:
        print(f'Error: {e}')

'''
Function : Main
'''
if __name__ == "__main__":
    drop_collection()
