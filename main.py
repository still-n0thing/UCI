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
    if request.method == "GET":
        return render_template('base.html')

app.run(host='localhost', port=5000)