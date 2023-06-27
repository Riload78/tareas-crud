
from flask import Blueprint, render_template, request, redirect, url_for, flash
import datetime
from models.entities.task import Task
from flask_login import login_required, current_user
from utils.db import db
from controller.email import Sendmail
from controller.queries import get_tasks, get_status, get_email

tasks = Blueprint('tasks',__name__)

@tasks.route('/list')
@login_required
def list_tasks():
    
    tasks = get_tasks()
    status = get_status()
    
    return render_template('list.html', tasks=tasks, name=current_user.username, status=status)
    

@tasks.route('/new', methods=['POST'])
@login_required
def new_task():
    title = request.form['title']
    description = request.form['description']
    date = datetime.datetime.utcnow()

    new_task = Task(title=title, description=description, user_id=current_user.id, status_id=1, create_at=date, updated_at=date)
    
    db.session.add(new_task)
    db.session.commit()
    
    flash('Task added succesfully', 'alert-success')
    return redirect(url_for('tasks.list_tasks'))


@tasks.route('/update/<id>', methods=['POST', 'GET'])
@login_required
def update(id):
    task = Task.query.get(id)

    if request.method == 'POST':
        date = datetime.datetime.utcnow()
        task.title = request.form['title']
        task.description = request.form['description']
        task.updated_at = date

        db.session.commit()
        flash('Tarea actualizado correctamente', 'alert-success')
        return redirect(url_for('tasks.list_tasks'))
    
    
    return render_template('update.html', task=task)

@tasks.route('/update-status/<id>', methods=['POST', 'GET'])
@login_required
def update_status(id):
    task = Task.query.get(id)

    if request.method == 'POST':
        task.status_id = request.form.get('status')
        task.user_id = request.form.get('user_id')
        print(request.form, id)
        
        
        db.session.commit()
        flash('Se actualizado el estado de la tarea', 'alert-success')
        user_email = get_email()

        email = Sendmail('Actualización de estado', [user_email])
        email.send_email('email/email_update_task.html', task=task)
        
            
        return redirect(url_for('tasks.list_tasks'))

@tasks.route('/delete/<id>')
def delete(id):
    contact = Task.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash('Tarea eliminada correctamente','alert-success')
    return redirect(url_for('tasks.list_tasks'))
