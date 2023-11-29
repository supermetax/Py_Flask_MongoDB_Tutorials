# run.py
from flask import Flask
from routes.admin import configure_admin_route
from routes.download import configure_download
from routes.landing import configure_landing_route
from routes.login import configure_login_route
from routes.signup import configure_signup_route

app = Flask(__name__)

# Configure routes
configure_landing_route(app)
configure_signup_route(app)
configure_login_route(app)
configure_admin_route(app)
configure_download(app)

if __name__ == '__main__':
    app.run(debug=True)
