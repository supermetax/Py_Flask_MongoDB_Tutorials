import hashlib
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
Function : hashing the password 
'''
def hash_password(password):
    # Use a strong hashing algorithm, such as SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

'''
Function : Find and delete user 
'''
def delete_user(userid, password):
    try:
        # Connect to MongoDB
        user_details = connect_to_mongodb()

        hash_pass = hash_password(password)

        if user_details:
            # Delete the user based on userid and password
            result = user_details.delete_one({'userid': userid, 'hashed_password': hash_pass})

            if result.deleted_count > 0:
                print(f"User with email {userid} deleted successfully.")
            else:
                print(f"User with email {userid} and password {password} not found.")
        else:
            print("Unable to connect to MongoDB. Check your connection details.")

    except Exception as e:
        print(f'Error: {e}')

'''
Function : Main
'''
if __name__ == "__main__":
    # Test deleting a user
    delete_user('user70@example.com', 'securepassword70')

