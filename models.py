from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Complaints(db.Model):
    __tablename__ = "COMPLAINTS"

    complaint_id = db.Column(db.Integer, primary_key = True)
    aadhar_id = db.Column(db.Integer)
    address = db.Column(db.String())
    postal_code = db.Column(db.Integer)
    complaint_type = db.Column(db.String())
    complaint_text =  db.Column(db.String(2048))


