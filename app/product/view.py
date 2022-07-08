import jwt
import os
import datetime
from flask import Blueprint, request
from .model import Product
from app.db import db
from app.commom import loginRequired, adminlogin
from werkzeug.utils import secure_filename

product_blueprint = Blueprint('product_blueprint',__name__)

#CREATE PRODUCT
@product_blueprint.route('/product', methods = ['POST'])
@adminlogin
def createProduct(userid):
    payload = request.json
    product = Product(name= payload['name'], details= payload['details'], quantity=payload['quantity'], price=payload['price'], imagepath= payload['imagepath'])
    product.created_by = userid
    db.session.add(product)
    db.session.commit()
    return {'Msg': 'Successfully created product'}

@product_blueprint.route('/product', methods= ['GET'])
def getAllProducts():
    try:
        product = Product.query.filter_by(is_deleted = False).all()
        productList = []
        for i in product:
            a = {
                'id': i.id,
                'name':i.name,
                'details':i.details,
                'quantity':i.quantity,
                'price':i.price,
                'imagepath': i.imagepath,
                'created_by':i.created_by,
                'created_date':i.created_date,
                'updated_by':i.updated_by,
                'updated_date':i.updated_date,
            }
            productList.append(a)
        return {'status': True, 'message':'Executed', 'data':productList}, 200
    except Exception as e:
        print("Error in get all product : ", e)
        return {'status': False, 'message':'Somthing wents wrong', 'data':''}, 200

@product_blueprint.route('/product/<id>', methods = ['GET'])
def getProductByID(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
            return {'status': True, 'message':' ', 'data':{}}, 200
        prdct ={
                'id': product.id,
                'name':product.name,
                'details':product.details,
                'quantity':product.quantity,
                'price':product.price,
                'imagepath': product.imagepath,
                'created_by':product.created_by,
                'created_date':product.created_date,
                'updated_by':product.updated_by,
                'updated_date':product.updated_date,
                'is_deleted':product.is_deleted
            }
        return {'status': True, 'message':'Executed', 'data':prdct}

    except:
        return {'status': False, 'message':'Somthing wents wrong', 'data':''}, 200
    

@product_blueprint.route('/product/upload/', methods=['POST'])
@adminlogin
def upload(userid):
    try:
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join('app','upload',filename))
        return {'imagepath': '/product/upload/'+filename}
    except Exception as e:
        print ("upload", e)
        return {'status': False, 'message':'something went wrong', 'data':None }


@product_blueprint.route('/product/<id>', methods= ['PUT'])
@loginRequired
def updateProduct(userid,id):
    try:
        payload = request.json
        product =  Product.query.filter_by(id=id).first()
        product.is_updated = True
        product.updated_date = datetime.datetime.now()
        product.updated_by = userid
        product.name= payload['name']
        product.price = payload['price']
        db.session.commit()
        return {'status': True, 'message':'Successfully Updated', 'data': '' }
    except Exception as e:
        print("update error", e)
        return {'status': False, 'message':'something went wrong', 'data':None }


@product_blueprint.route('/product/<id>' , methods= ['DELETE'])
@loginRequired
def deleteProduct(userid,id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
            return {"Satus" : True, "Message" : "No record found", "Data" : None}
        
        product.is_deleted = True
        db.session.commit()
        return {'Status': True, 'Message':'Deleted Successfully', 'Data':''}
    except Exception as e:
        print("delere error", e) 
        return {'status': False, 'message':'Something went wrong', 'data':None }