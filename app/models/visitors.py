from app import db

class visitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(20), unique=True, nullable=False)
    note = db.Column(db.String(255))
    shift = db.Column(db.String(50))
    call_back = db.Column(db.String(50))
    date = db.Column(db.Date)