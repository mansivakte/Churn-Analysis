import jwt
from flask import Blueprint, request
from flask_bcrypt import generate_password_hash,check_password_hash
from .model import User
from app.db import db
from app.commom import loginRequired

user_blueprint = Blueprint('user_blueprint', __name__)

#REGISTRARTION
@user_blueprint.route('/register', methods = ['POST'])
def register():
    payload = request.json
    validatorCheck = {}

    if payload['fname'] == '':
        validatorCheck.update({"Error": "First name is missing"})

    if payload['lname'] == '':
        validatorCheck.update({"Error": "Last name is missing"})
    
    if payload['email'] == '':
        validatorCheck.update({"Error": "EmailID name is missing"})

    if payload['password'] == '':
        validatorCheck.update({"Error": "Paaword name is missing"})

    if validatorCheck == {} : 
        user = User.query.filter_by(email = payload['email']).first()
        if user: 
            return {"Msg": "Email ID already registered"}
        else:
            user_password = generate_password_hash(payload['password'])
            user = User(email=payload['email'], password = user_password, fname=payload['fname'], lname= payload['lname'], admin=True)
            db.session.add(user)
            db.session.commit()
        return {"Msg" : "Registered Scessfully"}
    else:
        return {"Msg" : "Something wents wrong"}

#LOGIN
@user_blueprint.route('/login', methods = ['POST'])
def login():
    payload = request.json
    user = User.query.filter_by(email = payload['email']).first()
    if user:
        pw_hash = check_password_hash(user.password,payload['password'])
        if pw_hash:
            encoded_jwt = jwt.encode({'id':user.id, 'fname': user.fname, 'lname':user.lname}, "XYZ" , algorithm="HS256")
            return {'token': encoded_jwt}  ,200
        else:
            return {'Message': 'Invalid email/password'},401
    else:
        return {'Message': 'Invalid email/password'},401

#DASHBOARD
@user_blueprint.route('/dashboard', methods=['GET'])
@loginRequired
def dashboard(id):
    
    return "User Dashboard Page"



        
