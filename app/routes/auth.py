from flask import Blueprint,render_template, request, redirect, url_for, flash
from models.entities.task import User
from helpers.helper import create_password
from utils.db import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth',__name__)

@auth.route('/')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET','POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email= email).first()
    
    # if this returns a user, then the email already exists in database
    if user:
        
        flash('Este usuario ya existe.', 'alert-danger')
    else:
        if password:

            hash_pass = create_password(password)
            new_user = User(email=email, username=username, password=hash_pass)
        
            db.session.add(new_user)
            db.session.commit()
            flash('Gracias por registrarte.', 'alert-success')
    
    return render_template('auth/register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()    
    
        if not user or user.check_password(user.password, password) == False:
            flash('Usuario o password incorrectos.', 'alert-success')
            return redirect(url_for('auth.login')) 
        
        login_user(user, remember=True)
        return redirect(url_for('tasks.list_tasks')) 
    else:    
        return render_template('auth/login.html')
    
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))