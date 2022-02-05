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

class Transportation(db.Model):
    __tablename__ = "TRANSPORTATION"
    
    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"

class Agriculture(db.Model):
    __tablename__ = "AGRICULTURE"

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"

class DrinkingWater(db.Model):
    __tablename__ = "DrinkingWater".upper()

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"

class Electricity(db.Model):
    __tablename__ = "Electricity".upper()

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"

class Health(db.Model):
    __tablename__ = "Health".upper()

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"

class Security(db.Model):
    __tablename__ = "Security".upper()

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"

class Others(db.Model):
    __tablename__ = "Others".upper()

    id = db.Column(db.Integer, primary_key = True, unique = True)
    citizenship = db.Column(db.Integer, nullable = False)
    description = db.Column(db.Text, nullable = False)
    status = db.Column(db.Integer)

    # status
    #  0 == "Rejected"
    #  1 == "Not Approved Yes"
    #  2 == "Woring on it"
    #  3 == "Completed"

    def __init__(self, id, citizenship, description, status = 1) -> None:
        self.id = id
        self.citizenship = citizenship
        self.description = description
        self.status = status

    def __repr__(self) -> str:
        return f"({self.id}, {self.citizenship}, {self.description}, {self.status})"
