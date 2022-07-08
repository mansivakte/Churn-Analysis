from app.db import db

class Shopholder(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    shopname = db.Column(db.String(20))
    shopholdername = db.Column(db.String(40))
    email = db.Column(db.String(35))
    contactno = db.Column(db.Integer)
    

    def __init__(self, shopname, shopholdername, email, contactno):
        self.shopname = shopname
        self.shopholdername = shopholdername
        self.email = email
        self.contactno = contactno
        

    def __repr__(self):
        f'<User id:{self.id} shopname:{self.shopname} shopholdername:{self.shopholdername} email : {self.email} contactno: {self.contactno}>'
