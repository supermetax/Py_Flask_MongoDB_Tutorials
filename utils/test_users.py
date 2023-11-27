from db import get_all_users 

'''
Function : Main 
'''
if __name__ == "__main__":
   
   user = get_all_users()
   print(user)


# Function : To check user details
# user_data = check_user_credentials('user70@example.com','securepassword70')

# Function : To create a user in the DB
# add_user_to_db('user77@example.com', 'securepassword77')



# Function : To create a bulk number of users in the DB
# Test getting user details
# user_data = get_user_details('user70@example.com','securepassword70')
    
'''
if user_data:
    # Display user details in JSON format
    print(f"User {userid_to_check} exists!") 
    print(f"User details for {userid_to_check}:\n{user_data}")
else:
    print(f"User with email {userid_to_check} and password {password_to_check} not found.")
'''


# Function : To create a bulk number of users in the DB
'''
def create_10_users():
# Call the create_user function to add 10 records
    for i in range(1, 11):
        email = f'user{i}@example.com'
        password = f'securepassword{i}'
        create_user(email, password)
    print("10 records added successfully.")
'''


 