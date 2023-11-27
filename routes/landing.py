# routes/landing.py
from flask import render_template

def configure_landing_route(app):
    @app.route('/')
    def landing_page():
        return render_template('landing.html')
