from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Complaints(db.Models):
    __tablename__ = "COMPLAINTS"

    complaint_id = db.Column(db.Integer, primary_key = True)
    aadhar_id = db.Column(db.Integer)
    address = db.Column(db.String(1024))
    postal_code = db.Column(db.Integer)
    complaint_type = db.Column(db.String(64))

    
