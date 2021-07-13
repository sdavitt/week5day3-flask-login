# import our required packages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# import python modules for our database models

# we'll talk about security in a minute

# instantiate a database instance
db = SQLAlchemy()

# define a model - results in a database table
# whats happening in the parenthesis in the class line? We're inheriting behavior from a sqlalchemy class -> aka we're telling the computer "hey, this class is a database model"
class Animal(db.Model):
    # kind of similar to our CREATE TABLE queries -> we're telling the database what columns/attributes go into this table/model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    weight = db.Column(db.Integer, nullable=True, default='Unknown')
    height = db.Column(db.Integer, nullable=True, default='Unknown')
    climate = db.Column(db.String(50), nullable=True, default='all climates')
    region = db.Column(db.String(50))

    def __repr__(self):
        return f"<Animal: {self.name}>"