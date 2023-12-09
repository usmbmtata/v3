from app import db

class refer(db.Model):
    date = db.Column(db.Date)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    marker = db.Column(db.String(100))
    code = db.Column(db.Integer, primary_key=True)