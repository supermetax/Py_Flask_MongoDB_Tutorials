import hashlib
from pymongo import MongoClient, ASCENDING
from datetime import datetime
from faker import Faker
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
    

# Create an index on the 'userid' field with ASCENDING order (default is ASCENDING)
user_details = connect_to_mongodb()
user_details.create_index([('userid', ASCENDING)], unique=True)

'''
Function : To generate the Hashed Password
'''
def hash_password(password):
    # Use a strong hashing algorithm, such as SHA-256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


'''
Funtion : To check if the userid exists in the DB or not
'''
def is_userid_unique(userid):
    # Check if the userid is already present in the database
    return user_details.find_one({'userid': userid}) is None


'''
Funtion : To take random name from the list
'''
def generate_random_user_name():
    # Use faker to generate random names for plants, animals, or mountains
    fake = Faker()
    return fake.random_element(elements=(
        'Dog', 'Cow', 'Cat', 'Horse', 'Donkey', 'Tiger', 'Lion', 'Panther',
        'Leopard', 'Cheetah', 'Bear', 'Elephant', 'Polar bear', 'Turtle', 'Tortoise', 'Crocodile',
        'Rabbit', 'Porcupine', 'Hare', 'Hen', 'Pigeon', 'Albatross', 'Crow', 'Fish',
        'Dolphin', 'Frog', 'Whale', 'Alligator', 'Eagle', 'Flying squirrel', 'Ostrich', 'Fox',
        'Goat', 'Jackal', 'Emu', 'Armadillo', 'Eel', 'Goose', 'Arctic fox', 'Wolf',
        'Beagle', 'Gorilla', 'Chimpanzee', 'Monkey', 'Beaver', 'Orangutan', 'Antelope', 'Bat',
        'Badger', 'Giraffe', 'Hermit Crab', 'Giant Panda', 'Hamster', 'Cobra', 'Hammerhead shark', 'Camel',
        'Hawk', 'Deer', 'Chameleon', 'Hippopotamus', 'Jaguar', 'Chihuahua', 'King Cobra', 'Ibex',
        'Lizard', 'Koala', 'Kangaroo', 'Iguana', 'Llama', 'Chinchillas', 'Dodo', 'Jellyfish',
        'Rhinoceros', 'Hedgehog', 'Zebra', 'Possum', 'Wombat', 'Bison', 'Bull', 'Buffalo',
        'Sheep', 'Meerkat', 'Mouse', 'Otter', 'Sloth', 'Owl', 'Vulture', 'Flamingo',
        'Racoon', 'Mole', 'Duck', 'Swan', 'Lynx', 'Monitor lizard', 'Elk', 'Boar',
        'Lemur', 'Mule', 'Baboon', 'Mammoth', 'Blue whale', 'Rat', 'Snake', 'Peacock'
   ))

'''
Funtion : To (create and) add a user into the DB
'''
def add_user_to_db(email, password, language='English'):
    flag_code = 0

    # Check if the userid (email) is unique
    if not is_userid_unique(email):
        print(f"Error: User cannot be created. The userid '{email}' already exists in the database. Please try Login instead!")
        flag_code = 400
        return

    hashed_password = hash_password(password)
    user_name = generate_random_user_name()

    user_data = {
        'email': email,
        'hashed_password': hashed_password,
        'user_name': user_name,
        'userid': email,  # Use email as userid
        'date_of_creation': datetime.utcnow(),
        'date_of_last_login': None,
        'date_of_last_update': None,
        'language_preference': language
    }
    user_details.insert_one(user_data)
    print(f"User with userid '{email}' created in the database.")
    flag_code = 200

    return flag_code


'''
Function : To check if the user exists and return the details 
'''
def get_user_details(userid, password):
    try:
        user_details = connect_to_mongodb()
        hash_pass = hash_password(password)      
        # Query the user details based on email and password
        user_data = user_details.find_one({'userid': userid, 'hashed_password': hash_pass})
        return user_data

    except Exception as e:
        print(f'Error: {e}')
        return None


'''
Function : To check if the use exists + Save the login date-time in the DB
'''
def check_user_credentials(userid, password):
    try:
        user_details = connect_to_mongodb()
        hashed_password = hash_password(password)
        user = user_details.find_one({'userid': userid, 'hashed_password': hashed_password})
        if user:
            # Update last login date
            user_details.update_one({'_id': user['_id']}, {'$set': {'date_of_last_login': datetime.utcnow()}})
            print("User authenticated successfully.")
            return True
        else:
            return False

    except Exception as e:
        print(f'Error: {e}')
        return None


'''
Function : To retrieve all users from the DB
'''
def get_all_users():
    try:
        user_details = connect_to_mongodb()
        user = user_details.find({}, {'_id': 0})  
        return user

    except Exception as e:
        print(f'Error: {e}')
        return None


'''
if __name__ == "__main__":
    
cursor = get_all_users()
# Iterate over the cursor
for document in cursor:
    # Process each document here
    print(document)

'''