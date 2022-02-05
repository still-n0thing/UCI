from flask import Flask, render_template, request, redirect, abort
from models import Agriculture, DrinkingWater, Electricity, Health, Others, Security, Transportation, db, Complaints

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


        # Checking which table should this data be stored

        # print(obj) # returned as a tuple
        # print(type(obj))
        if category == "Transportation":
            comp_tb = Transportation(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()
        elif category == "Agriculture":
            comp_tb = Agriculture(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()
        elif category == "Drinking Water":
            comp_tb = DrinkingWater(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()
        elif category == "Electricity":
            comp_tb = Electricity(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()
        elif category == "Health":
            comp_tb = Health(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()
        elif category == "Security":
            comp_tb = Security(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()
        else:
            comp_tb = Others(id = obj.id, citizenship= obj.citizenship, description = obj.description)
            db.session.add(comp_tb)
            db.session.commit()

        return render_template('index.html', complaint_data = complaint)

@app.route('/feedback', methods = ["GET", "POST"])
def feedback():
    if request.method == "GET":
        return render_template('feedback.html')
    
    if request.method == "POST":
        comp_id = request.form["complaintId"]
        comp_id = int(comp_id)
        comp_obj = db.session.query(Complaints).filter(Complaints.id == comp_id).first()
        # print(db.session.query(Complaints).filter(Complaints.id == comp_id).first())
        category = None
        if comp_obj != None:
            category = comp_obj.category
        # print(comp_id)
        # print(category)

        obj = None
        if category == "Transportation":
            obj = db.session.query(Transportation).filter(Transportation.id == comp_id).first()         
        elif category == "Agriculture":
            obj = db.session.query(Agriculture).filter(Agriculture.id == comp_id).first()
        elif category == "Drinking Water":
            obj = db.session.query(DrinkingWater).filter(DrinkingWater.id == comp_id).first()
        elif category == "Electricity":
            obj = db.session.query(Electricity).filter(Electricity.id == comp_id).first()
        elif category == "Health":
            obj = db.session.query(Health).filter(Health.id == comp_id).first()
        elif category == "Security":
            obj = db.session.query(Security).filter(Security.id == comp_id).first()
        elif obj == "Others":
            obj = db.session.query(Others).filter(Others.id == comp_id).first()

        # STATUS (num : meaning)
        dt = { 
            0 : "Your Complaint was rejected please try again with correct information",
            1 : "Your Complaint is yet to be approved",
            2 : "We are working on your Complaint",
            3 : "Work on your Compaint is finished"
        }
        if obj != None:
            return render_template('feedback.html', data = {
                "to_display" : dt[obj.status]
            })
        else:
            return render_template('feedback.html', data = {
                "to_display": "Invalid Reference ID"
            })

@app.route('/login', methods = ["GET", "POST"])
def login():
    admins_db = {
        "transportation@gov.in":{
            "password" : "password",
            "type" : "Transportation"
        },
        "agriculture@gov.in":{
            "password" : "password",
            "type" : "Agriculture"
        },
        "drinkingwater@gov.in":{
            "password" : "password",
            "type" : "DrinkingWater"
        },
        "electricity@gov.in":{
            "password" : "password",
            "type" : "Electricity"
        },
        "health@gov.in":{
            "password" : "password",
            "type" : "Health"
        },
        "security@gov.in":{
            "password" : "password",
            "type" : "Security"
        },
        "others@gov.in":{
            "password" : "password",
            "type" : "Others"
        }
    }

    if request.method == "GET":
        return render_template('login.html')
    
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        category = None
        if email.lower() in admins_db:
            if password == admins_db[email.lower()]['password']:
                category = admins_db[email.lower()]['type']

        if category != None:
            # print("Login Sucess")
            return redirect(f'/table/{category}')
        else:
            # print("Login Failed")
            return render_template('login.html')

@app.route('/table/<string:category>', methods = ["GET", "POST"])
def table(category):
    all_types = {
        "Transportation" : Transportation,
        "Agriculture" : Agriculture,
        "DrinkingWater" : DrinkingWater,
        "Electricity": Electricity,
        "Health": Health,
        "Security": Security,
        "Others": Others
    }
    
    in_expression = all_types[category].status.in_([1, 2, 3])
    lst_of_complaints = db.session.query(all_types[category]).filter(in_expression)

    opt = [
        "Rejected",
        "Pending",
        "InProgress",
        "Finished"
    ]

    if lst_of_complaints:
        nm = ""
        if category == "DrinkingWater":
            nm = "Drinking Water"
        else:
            nm = category
        return render_template('table.html', obj = {
            "data" : lst_of_complaints,
            "to_display": opt,
            "page_name" : nm,
            "page_id" : category
        })


@app.route('/table/<string:category>/<int:id>', methods = ["POST", "GET"])
def update_status(category, id):
    all_types = {
        "Transportation" : Transportation,
        "Agriculture" : Agriculture,
        "DrinkingWater" : DrinkingWater,
        "Electricity": Electricity,
        "Health": Health,
        "Security": Security,
        "Others": Others
    }

    opt = {
        "Rejected" : 0,
        "Pending" : 1,
        "InProgress" : 2,
        "Finished" : 3,
    }

    if request.method == "POST":
        status = request.form["status"]
        changing_row = all_types[category].query.get_or_404(id)
        changing_row.status = opt[status]

        try:
            db.session.commit()
            return redirect(f'/table/{category}')
        except:
            return 'There is some issus'

    else:
        return redirect(f'/table/{category}')

# Working 
@app.route('/list')
def all_complaints():
    lst_of_complaints = Transportation.query.all()
    # users = Transportation.query.all()

    opt = [
        "Rejected",
        "Pending",
        "In Progress",
        "Finished"
    ]
    print(lst_of_complaints)
    if lst_of_complaints:
        return render_template('table.html', obj = {
            "data" : lst_of_complaints,
            "to_display": opt
        })


# For Heroku
def getApp():
    return app

# No need to change this before the deployment
if __name__ == "__main__":
    app.run(debug=True)