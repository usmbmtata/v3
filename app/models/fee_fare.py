from app import db


class Fee_Fare(db.Model):
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

    