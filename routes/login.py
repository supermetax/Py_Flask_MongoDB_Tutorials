# routes/signup.py
from flask import redirect, render_template, request, url_for
from db import check_user_credentials

def configure_login_route(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # Check user credentials
            if check_user_credentials(email, password):
                # Redirect to the main landing page with the user's welcome message
                return redirect(url_for('download'))
            else:
                return "Invalid login credentials. Please try again."

        return render_template('login.html')
    

