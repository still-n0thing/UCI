from enum import unique
from unicodedata import category
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Complaints(db.Model):
    __tablename__ = "COMPLAINTS"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    category = db.Column(db.String, nullable = False)
    description = db.Column(db.Text, nullable = False)


    def __init__(self, citizenship, category, description) -> None:
        self.citizenship = citizenship
        self.category = category
        self.description = description

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.category}, {self.description})"
    
# TODO: Implement all the tables with complaint_id as Foreign Key

# class Transportation(db.Model):
#     pass

# class Agriculture(db.Model):
#     pass

# class DrinkingWater(db.Model):
#     pass

# class Electricity(db.Model):
#     pass

# class Health(db.Model):
#     pass

# class Security(db.Model):
#     pass

# class Others(db.Model):
#     pass