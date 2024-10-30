from flask import Flask
from flask_cors import CORS

from app.config import Config

# Create a Flask app
app = Flask(__name__)

# This will enable CORS for all routes and domains
CORS(app, supports_credentials=True)

# Load the config from the config.py file
app.config.from_object(Config)

# Import the routes
from app.routes import get
