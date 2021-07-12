# import necessary packages/modules (in this case the Flask class and Config class)
from flask import Flask
from config import Config

# import our Blueprint object from the blueprint's routes file
from .site.routes import site
from .authentication.routes import auth


# define our application as instance of the Flask object
app = Flask(__name__)

# register our blueprints
app.register_blueprint(site)
app.register_blueprint(auth)

# configure our application based on the Config class from the config.py file
app.config.from_object(Config)