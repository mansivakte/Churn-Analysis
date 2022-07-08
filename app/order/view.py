import uuid
import datetime
from app.db import db
from flask import Blueprint, request
from .model import Order
from app.orderdetails.model import Orderdetails
from app.shopholders.model import Shopholder
from app.product.model import Product
from app.commom import loginRequired
import pdfkit


order_blueprint = Blueprint('order_blueprint', __name__)


#Create Order
@order_blueprint.route('/order', methods=['POST'])
@loginRequired
def createOrder(userid):

    payload = request.json
    shopholder_id  = payload['order_details']['shopholder_id']
    product = payload['order_details']['product']
    # print("1.shopholder_id ", shopholder_id)
    # print("2.product ", product)
   
    total = 0
    for i in product:
        prod = Product.query.filter_by(id=i['product_id']).first()

        total += (prod.price * i['qty'])

    order= Order(amount = total, order_id= str(uuid.uuid1()), order_date=datetime.datetime.now())
    order.user_id= userid
    db.session.add(order)
    db.session.commit()
    
    pdfkit.from_string('MANSI Vakte Order','mansi.pdf')

#orderdetails
    for i in product:
        prdct = Product.query.filter_by(id = i['product_id']).first()
        # print(type(prdct))
        # print("1. prod : ", prdct)
        orderdetails = Orderdetails(
            order_id=order.order_id,
            product_id = i['product_id'],
            product_price = prdct.price,
            product_qty = i['qty'],
            total_price = (prdct.price * i['qty'])
        )
        # print("2. orderdetails",orderdetails)
        # print("3. ", prdct)
        # print("4 . ", type(i['qty']))
        quantity = int(prdct.quantity) - int(i['qty'])
        prdct.quantity = quantity
        # print("5. quantity :", quantity)
        db.session.add(orderdetails)
        db.session.commit()

    return {"status": "order is created"}


#get all order
@order_blueprint.route('/order', methods=['GET'])
def getOrder():

    order = Order.query.all()
    odr = []
    for i in order:
        a = {
            'id':i.id,
            'amount':i.amount,
            'order_id':i.order_id,
            'order_date':i.order_date
        }
        odr.append(a)
    return {"data": odr}


#get orderdetails
@order_blueprint.route('/orderdetails', methods=['GET'])
def getOrderdetails():

    orderdetails = Orderdetails.query.all()
    odr = []
    for i in orderdetails:
        a = {
            'id':i.id,
            'order_id':i.order_id,
            'product_id':i.product_id,
            'product_price':i.product_price,
            'product_qty': i.product_qty,
            'total_price': i.total_price
        }
        odr.append(a)
    return {"data": odr}