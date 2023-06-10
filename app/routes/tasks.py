
from flask import Blueprint,render_template, request, redirect, url_for, flash
import datetime
from models.entities.task import Task
from flask_login import login_required, current_user
from utils.db import db

tasks = Blueprint('tasks',__name__)

@tasks.route('/list')
@login_required
def list_tasks():
    tasks = Task.query.filter_by(user_id=current_user.id)
    return render_template('list.html', tasks=tasks, name=current_user.username)
    

@tasks.route('/new', methods=['POST'])
@login_required
def new_task():
    title = request.form['title']
    description = request.form['description']
    date = datetime.datetime.utcnow()

    new_task = Task(title=title, description=description, user_id=current_user.id, status=1, create_at=date, updated_at=date)
    
    db.session.add(new_task)
    db.session.commit()
    
    flash('Task added succesfully')
    return redirect(url_for('tasks.list_tasks'))


@tasks.route('/update/<id>', methods=['POST', 'GET'])
@login_required
def update(id):
    task = Task.query.get(id)
    if request.method == 'POST':
       
        task.title = request.form['title']
        task.email = request.form['description']

        db.session.commit()
        
        return redirect(url_for('taks.index'))
    
    
    return render_template('update.html', task=task)

@tasks.route('/delete/<id>')
def delete(id):
    contact = Task.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Contact Deleted succesfully')
    return redirect(url_for('contacts.index'))
