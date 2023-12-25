from app import db

class fee_coll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(20), unique=True, nullable=False)
    reg_no = db.Column(db.String(10), db.ForeignKey('student.reg_no'))
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