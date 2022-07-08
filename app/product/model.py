import datetime
from app.db import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50))
    details = db.Column(db.Text)
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)
    imagepath = db.Column(db.String(80))
    created_by = db.Column(db.Integer, default = 0)
    created_date = db.Column(db.DateTime(timezone=True),default=datetime.datetime.utcnow)
    updated_by = db.Column(db.Integer, default = 0)
    updated_date = db.Column(db.DateTime(timezone=True), default=None)
    is_updated =db.Column(db.Boolean, default=False)
    is_deleted = db.Column(db.Boolean, default=False)
    

    def __init__(self,name,details, quantity, price, imagepath):
        self.name = name
        self.details = details
        self.quantity = quantity
        self.price = price
        self.imagepath = imagepath

    def __repr__(self):
        return f'<Product id:{self.id} name:{self.name} details:{self.details} quantity:{self.quantity} price:{self.price} imagepath:{self.imagepath}>'
