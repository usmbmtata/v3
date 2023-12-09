from app import db

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
