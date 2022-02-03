from mimetypes import common_types
from flask import Flask, render_template, request, redirect, abort
from models import db, Complaints

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

@app.route('/', methods = ["GET", "POST"])
def create_complaints():
    
    # Debug Section
    # lst = employees = Complaints.query.all()
    # print(lst)
    # Debug Section

    if request.method == "GET":
        return render_template('front-page.html')

    if request.method == "POST":
        aadhar_id = request.form['aadhar_id']
        name = request.form['name']
        phoneno = request.form['phoneno']
        address = request.form['address']
        postal_code = request.form['postal_code']
        complaint_type = request.form['complaint_type']
        complaint_text =  request.form['complaint_text']
        complaint = Complaints(
            aadhar_id=aadhar_id, name=name, phoneno=phoneno, 
            address=address, postal_code=postal_code,
            complaint_type=complaint_type, complaint_text=complaint_text
        )
        # print(complaint)
        db.session.add(complaint)
        db.session.commit()
        return render_template('front-page.html')



# For Heroku
def getApp():
    return app

# Need to be configured before hosting
app.run(host='localhost', port=5000)