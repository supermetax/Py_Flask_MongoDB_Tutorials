# routes/signup.py
from flask import render_template, request
from db import add_user_to_db

def configure_signup_route(app):
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # Call the function from db.py to add user to the database
            db_code = add_user_to_db(email, password)

            if db_code == 200:
                return "Signup for user: " + email + " is successful! User details added to the database."
            if db_code == 400:
                return "Error: User cannot be created. The user: " + email + "already exists in the database. Please try Login instead!"
            else:
                return "Error adding user: " + email + " to the database. Please try again." 
        return render_template('signup.html')
    

