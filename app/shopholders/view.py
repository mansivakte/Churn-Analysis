import jwt
import os
import datetime
from flask import Blueprint, request
from .model import Shopholder
from app.db import db
from app.commom import loginRequired


shopholder_blueprint = Blueprint('shopholder_blueprint', __name__)

@shopholder_blueprint.route('/shopholder', methods = ['POST'])
@loginRequired
def createShopHolders(userid):
    payload = request.json
    shopholder = Shopholder(shopname= payload['shopname'], shopholdername=payload['shopholdername'], email=payload['email'], contactno=payload['contactno'])
    shopholder.created_by = userid
    db.session.add(shopholder)
    db.session.commit()
    return {'Msg': 'Successfully created shopholder'}
