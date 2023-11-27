# routes/admin.py
from flask import render_template, request, redirect, url_for
from db import check_user_credentials, get_all_users

def configure_admin_route(app):
    @app.route('/admin', methods=['GET', 'POST'])
    def admin_login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            # Check admin credentials
            if check_user_credentials(email, password) and email == 'admin@admin.com':
                # Redirect to the admin landing page
                return redirect(url_for('admin_landing'))
            else:
                return "Invalid login credentials. Please try again."

        return render_template('admin_login.html')

    @app.route('/admin/landing')
    def admin_landing():
        # Get all users from the database
        cursor = get_all_users()

        return render_template('admin_landing.html', cursor=cursor)
