from models.entities.task import Task, Status, User
from flask_login import current_user
from utils.db import db

def get_tasks():
    tasks = db.session.query(Task, Status.name).\
        join(Status, Status.id == Task.status_id).\
        filter(Task.user_id == current_user.id).all()
        
    return tasks

def get_status():
    status = Status.query.all()
    
    return status

def get_email():
    user = User.query.filter_by(id=current_user.id).first()
    if user:
        email = user.email
    return email