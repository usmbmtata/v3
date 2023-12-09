from app import db

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
    code = db.Column(db.String(10), nullable=True)
    aadhar_number = db.Column(db.String(16))
    mode = db.Column(db.String(20))
    notice = db.Column(db.String(10))