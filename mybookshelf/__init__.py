from flask import Flask
from flask_failsafe import failsafe

@failsafe
def create_app():
	app = Flask(__name__)
	with app.app_context():
		from . import routes
		return app
