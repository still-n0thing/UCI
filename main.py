from flask import Flask, render_template, request, redirect, abort
from models import db, Complaints

app = Flask(__name__)

db_file_name = "data.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# TODO: need to add session ref = https://www.geeksforgeeks.org/how-to-use-flask-session-in-python-flask/ for login page 

# setup so that database is created 
@app.before_first_request
def create_table():
    import os
    if not os.path.exists(db_file_name): 
        db.create_all()

# Working
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

# Working 
@app.route('/list')
def all_complaints():
    lst_of_complaints = Complaints.query.all()
    if lst_of_complaints:
        return render_template('display-entries.html', lst_of_complaints=lst_of_complaints)

# TODO: index, login, feedback need to routed, POST request needs to handled and html need editing
@app.route('/index')
def testing_stuff():
    if request.method == "GET":
        # return render_template('some.html')
        return render_template('index.html')

@app.route('/login')
def login_page():
    if request.method == "GET":
        return render_template('login.html')

@app.route('/feedback')
def feedback_page():
    if request.method == "GET":
        return render_template('feedback.html')

# For Heroku
def getApp():
    return app

# No need to change this before the deployment
if __name__ == "__main__":
    app.run(debug=True)