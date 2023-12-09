from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/veda2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), unique=True, nullable=False)
    note = db.Column(db.String(255))
    shift = db.Column(db.String(50))
    call_back = db.Column(db.String(50))
    date = db.Column(db.Date)

class student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reg_no = db.Column(db.String(15), unique=True, nullable=False)
    reg_date = db.Column(db.Date)
    pay_date = db.Column(db.Date)
    name = db.Column(db.String(100))
    course = db.Column(db.String(100))
    contact = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100))
    gender = db.Column(db.String(10))
    registration_fee = db.Column(db.Float)
    address = db.Column(db.String(255))
    code = db.Column(db.Integer, db.ForeignKey('fee_fare.s_no'))
    aadhar_number = db.Column(db.String(16))
    mode = db.Column(db.String(20))
    notice = db.Column(db.String(10))

    # Define relationships with other tables
    visitor_id = db.Column(db.Integer, db.ForeignKey('visitor.id'))
    visitor = db.relationship('visitor', backref='students')

    fee_coll = db.relationship('fee_coll', backref='student')

# Define the rest of the tables with their respective fields and relationships
class fee_coll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(15), unique=True, nullable=False)
    fee_time = db.Column(db.Date)
    payment_time = db.Column(db.Date)
    username = db.Column(db.String(100), db.ForeignKey('admin.name'))
    name = db.Column(db.String(100))
    contact = db.Column(db.String(20))
    month = db.Column(db.String(20))
    rate = db.Column(db.Float)
    type = db.Column(db.String(20))
    slot = db.Column(db.String(20))
    status = db.Column(db.String(3))

class admin(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(20))

class galla(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    open_bal = db.Column(db.Float)
    reg_fee = db.Column(db.Float)
    fee_coll = db.Column(db.Float)
    exp = db.Column(db.Float)
    inc = db.Column(db.Float)
    deposit = db.Column(db.Float)
    close_bal = db.Column(db.Float)
    date = db.Column(db.Date)

class fee_fare(db.Model):
    s_no = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    type_a = db.Column(db.Float)
    type_b = db.Column(db.Float)
    type_c = db.Column(db.Float)
    type_d = db.Column(db.Float)
    type_e = db.Column(db.Float)
    type_a1 = db.Column(db.Float)
    type_b1 = db.Column(db.Float)
    type_c1 = db.Column(db.Float)
    type_d1 = db.Column(db.Float)
    type_e1 = db.Column(db.Float)

class refer(db.Model):
    date = db.Column(db.Date)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    marker = db.Column(db.String(100))
    code = db.Column(db.Integer, primary_key=True)

with app.app_context():
    db.create_all()