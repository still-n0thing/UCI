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
        return render_template('index.html')

    if request.method == "POST":
        citizenship = request.form['citizenship']
        category = request.form['category']
        description = request.form['description']
        complaint = Complaints(
            citizenship = citizenship, category = category, description = description 
        )
        # print(complaint)
        db.session.add(complaint)
        db.session.commit()
        obj = db.session.query(Complaints).order_by(Complaints.id.desc()).first()
        # working on this 
        # print(obj) # returned as a tuple
        return render_template('index.html', complaint_data = complaint)

# Working 
@app.route('/list')
def all_complaints():
    lst_of_complaints = Complaints.query.all()
    if lst_of_complaints:
        return render_template('display-entries.html', lst_of_complaints=lst_of_complaints)

# For Heroku
def getApp():
    return app

# No need to change this before the deployment
if __name__ == "__main__":
    app.run(debug=True)