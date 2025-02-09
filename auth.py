from flask import Blueprint, render_template, redirect, request
from flask_mail import Message
from . import db, mail, bcrypt

import random

otp = random.randrange(100000, 999999)
username = ''
email = ''
password = ''

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        info = db.accounts.find_one({'email': email})
        if (info is None):
            message = 'user does not exist'
        else:
            hashed_passwd = info['password']
            if (bcrypt.check_password_hash(hashed_passwd, password)):
                db.accounts.update_one(
                    {"email": email},
                    {"$set": {"logged_in": True}}
                )
                return redirect('/')
            else:
                message = 'incorrect password'
                
    return render_template('login.html', message=message)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    global username, email, password, otp
    message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if (email == db.accounts.find_one({'email': email})):
            message = 'user already exists'
        if len(username) < 3:
            message = 'username too short'
        elif len(password) < 7:
            message = 'password too short'
        elif (password != confirm_password):
            message = 'passwords do not match'
        else:
            msg = Message("OTP for email confirmation", sender='noreply@gmail.com', recipients=[email])
            msg.body = str(otp)
            mail.send(msg)
            return redirect('/verify')
        
    return render_template('signup.html', message=message)

@auth.route('/verify', methods=['GET', 'POST'])
def verify():
    global otp, username, email, password
    message = ''
    if request.method == 'POST':
        passwd = request.form.get('otp')
        if passwd == str(otp):
            hashed_password = bcrypt.generate_password_hash(password)
            db.accounts.insert_one(
                {
                    "email": email,
                    "username": username,
                    "password": hashed_password,
                    "cart": [],
                    "logged_in": True
                }
            )
            
            return redirect('/')
        else:
            message = 'incorrect otp'
        
    return render_template('verify.html', message=message)

@auth.route('/logout')
def logout():
    user = db.accounts.find_one({'logged_in': True})
    db.accounts.update_one({"username": user['username']}, {'$set': {'logged_in': False}})
    return redirect('/')