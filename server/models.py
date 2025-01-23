from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Metadata for database schema
metadata = MetaData()

# Create the Flask SQLAlchemy extension with the specified metadata
db = SQLAlchemy(metadata=metadata)

# Define a model class by inheriting from db.Model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
