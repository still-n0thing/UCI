from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import true

db = SQLAlchemy()

class Complaints(db.Model):
    __tablename__ = "COMPLAINTS"

    id = db.Column(db.Integer, primary_key = True)
    aadhar_id = db.Column(db.Integer, unique = True)
    name = db.Column(db.String())
    phoneno = db.Column(db.Integer())
    address = db.Column(db.String())
    postal_code = db.Column(db.Integer)
    complaint_type = db.Column(db.String())
    complaint_text =  db.Column(db.String(2048))

    def __init__(self, aadhar_id, name, phoneno, address, postal_code, complaint_type, complaint_text) -> None:
        self.aadhar_id = aadhar_id
        self.name = name
        self.phoneno = phoneno
        self.address = address
        self.postal_code = postal_code
        self.complaint_type = complaint_type
        self.complaint_text = complaint_text
    
    def __repr__(self) -> str:
        return f"({self.aadhar_id}, {self.name}, {self.phoneno}, {self.address}, {self.postal_code}, {self.complaint_type}, {self.complaint_text})"

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