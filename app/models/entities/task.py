from utils.db import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(300))
    tasks = db.relationship('Task', backref='user', lazy=True)
    
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def check_password(self, hashed_pass, password):
        result = check_password_hash(hashed_pass, password)
        
        return result
    
        
       
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(100))
    description = db.Column(db.Text)
    create_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    
    def __init__(self, title, description, user_id, status_id, create_at, updated_at):
       self.title = title
       self.description = description
       self.user_id = user_id
       self.status_id = status_id
       self.create_at = create_at
       self.updated_at = updated_at
           
class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    tasks= db.relationship("Task", backref='status', lazy=True)
    
    def __init__(self, status_name):
        self.status_name = status_name
        
    def get_status(self):
        status = Status.query.all
        return status
    
   
    
    
    
    
    