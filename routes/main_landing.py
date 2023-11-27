# routes/main_landing.py
from flask import render_template

def configure_main_landing_route(app):
    @app.route('/main_landing/<user>')
    def main_landing(user):
        return render_template('main_landing.html', user=user)
