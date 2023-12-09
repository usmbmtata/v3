from app import db

class Admin(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    role = db.Column(db.String(20))
    chat_id = db.Column(db.String(255))
    email = db.Column(db.String(255))