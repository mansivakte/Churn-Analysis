from app.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fname = db.Column(db.String(20))
    lname = db.Column(db.String(20))
    email = db.Column(db.String(35))
    password = db.Column(db.String(80))
    admin = db.Column(db.Boolean, default=False)

    def __init__(self, fname, lname, email, password, admin):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password
        self.admin = admin

    def __repr__(self):
        f'<User id:{self.id} fname:{self.fname} lname:{self.lname} is_admin:{self.admin}>'
