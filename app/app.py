from flask import Flask
from routes.tasks import tasks
from routes.auth import auth
from flask_login import LoginManager
from config import DevelopmentConfig, Config
from models.entities.task import User
from flask_mail import Mail

app = Flask(__name__)
mail = Mail()

app.secret_key = Config.SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/tasks_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True

app.config['MAIL_SERVER'] = Config.MAIL_SERVER
app.config['MAIL_PORT'] = Config.MAIL_PORT
app.config['MAIL_USE_TLS'] = Config.MAIL_USE_TLS
app.config['MAIL_USERNAME'] = Config.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = Config.MAIL_PASSWORD

app.register_blueprint(tasks)
app.register_blueprint(auth)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)



@login_manager.user_loader
def load_user(user_id):
     # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

