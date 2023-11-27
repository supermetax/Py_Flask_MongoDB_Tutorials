from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

'''
Function : To create a connection to the DB, then create a new collectipon and then drop/ delete the DB
'''
# Access MongoDB URI from environment variables
mongo_uri = os.getenv('MONGODB_URI')

def test_mongodb_connection():
    try:
        # Create a MongoClient and test the connection
        client = MongoClient(mongo_uri)
        db = client.test_database
        collection = db.test_collection
        collection.insert_one({'test_key': 'test_value'})
        result = collection.find_one({'test_key': 'test_value'})
        
        # Check if the test document was inserted and retrieved successfully
        if result and result['test_key'] == 'test_value':
            print('Connected to MongoDB Cloud successfully!')
        else:
            print('Failed to insert and retrieve test document.')
        
        # Clean up: drop the test collection
        db.drop_collection('test_collection')

    except Exception as e:
        print(f'Error: {e}')

'''
Function : Main
'''
if __name__ == "__main__":
    test_mongodb_connection()
